/**
 * Convert ByteByteGo OOD course JSON files to Markdown.
 * Evaluates the compiled JSX code with a mock runtime that generates markdown.
 * Images are referenced with full URLs; use download_images.py to localize them.
 */
import { readFileSync, writeFileSync, readdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const RAW_DIR = join(__dirname, 'raw_json');
const OUT_DIR = __dirname;
const BASE_URL = 'https://bytebytego.com';

function createMockRuntime() {
  let listDepth = 0;
  let listStack = [];
  let orderedList = false;
  let listItemIndex = 0;
  let insidePre = false;

  function renderChildren(children) {
    if (children === null || children === undefined) return '';
    if (typeof children === 'string') return children;
    if (typeof children === 'number') return String(children);
    if (Array.isArray(children)) return children.map(renderChildren).join('');
    if (typeof children === 'object' && '__md' in children) return children.__md;
    if (typeof children === 'object') return '';
    return String(children);
  }

  function jsx(type, props) {
    const tag = typeof type === 'string' ? type : type?.__name || '';

    // Skip aria-hidden spans (katex-html visual duplicates) BEFORE katex check
    if (tag === 'span' && props?.['aria-hidden'] === 'true') return { __md: '' };

    // KaTeX: extract just the annotation text (LaTeX source), skip visual duplication
    if (tag === 'span' && props?.className) {
      const cls = props.className;
      if (cls === 'katex' || cls.includes('katex')) {
        return { __md: renderChildren(props?.children) };
      }
    }

    // Skip strut/spacing spans with no text content
    if (tag === 'span' && props?.style && !props?.children) return { __md: '' };

    const children = renderChildren(props?.children);

    switch (tag) {
      case 'h1': return { __md: `\n# ${children}\n` };
      case 'h2': return { __md: `\n## ${children}\n` };
      case 'h3': return { __md: `\n### ${children}\n` };
      case 'h4': return { __md: `\n#### ${children}\n` };
      case 'h5': return { __md: `\n##### ${children}\n` };
      case 'p': {
        if (listDepth > 0) return { __md: children };
        return { __md: `\n${children}\n` };
      }
      case 'em': return { __md: `*${children}*` };
      case 'strong': return { __md: `**${children}**` };
      case 'code': {
        if (insidePre) return { __md: children };
        return { __md: `\`${children}\`` };
      }
      case 'pre': {
        insidePre = true;
        const inner = renderChildren(props?.children);
        insidePre = false;
        const stripped = inner.startsWith('`') && inner.endsWith('`')
            ? inner.slice(1, -1) : inner;
        return { __md: `\n\`\`\`\n${stripped}\n\`\`\`\n` };
      }
      case 'br': return { __md: '\n' };
      case 'hr': return { __md: '\n---\n' };
      case 'a': {
        const href = props?.href || '';
        return { __md: `[${children}](${href})` };
      }
      case 'blockquote': return { __md: `\n> ${children.replace(/\n/g, '\n> ')}\n` };
      case 'ul': {
        listStack.push({ orderedList, listItemIndex });
        listDepth++;
        orderedList = false;
        listItemIndex = 0;
        const result = renderChildren(props?.children);
        listDepth--;
        ({ orderedList, listItemIndex } = listStack.pop());
        return { __md: `\n${result}` };
      }
      case 'ol': {
        listStack.push({ orderedList, listItemIndex });
        listDepth++;
        orderedList = true;
        listItemIndex = 0;
        const result = renderChildren(props?.children);
        listDepth--;
        ({ orderedList, listItemIndex } = listStack.pop());
        return { __md: `\n${result}` };
      }
      case 'li': {
        listItemIndex++;
        const indent = '  '.repeat(Math.max(0, listDepth - 1));
        const bullet = orderedList ? `${listItemIndex}.` : '-';
        const trimmed = children.replace(/^\n+/, '').replace(/\n+$/, '').replace(/\n/g, '\n' + indent + '  ');
        return { __md: `${indent}${bullet} ${trimmed}\n` };
      }
      case 'table': return { __md: `\n${children}\n` };
      case 'thead': {
        const trimmed = children.trim();
        const colCount = Math.max(1, (trimmed.match(/\|/g) || []).length - 1);
        const sep = '| ' + Array(colCount).fill('---').join(' | ') + ' |';
        return { __md: trimmed + '\n' + sep + '\n' };
      }
      case 'tbody': return { __md: children };
      case 'tr': {
        const rawChildren = props?.children;
        let childArr;
        if (Array.isArray(rawChildren)) childArr = rawChildren;
        else if (rawChildren !== null && rawChildren !== undefined) childArr = [rawChildren];
        else childArr = [];
        const cells = childArr.map(c => {
          const text = renderChildren(c);
          return flattenCell(text);
        });
        if (cells.length === 0) return { __md: '' };
        return { __md: `| ${cells.join(' | ')} |\n` };
      }
      case 'th':
      case 'td': return { __md: children };
      case 'sup': return { __md: children };
      case 'sub': return { __md: children };
      case 'span': return { __md: children };
      case 'div': return { __md: `\n${children}\n` };
      case 'img': {
        const src = props?.src || '';
        const alt = (props?.alt || 'image').substring(0, 120);
        const fullSrc = src.startsWith('/') ? BASE_URL + src : src;
        return { __md: `\n![${alt}](${fullSrc})\n` };
      }
      // KaTeX math elements
      case 'math':
      case 'semantics':
        return { __md: children };
      case 'mrow':
      case 'mn':
      case 'mo':
      case 'mi':
      case 'msup':
      case 'msub':
      case 'mfrac':
      case 'mtext':
        return { __md: '' };
      case 'annotation':
        return { __md: children };
      // Custom components
      case 'Figure': {
        const caption = props?.caption || '';
        if (caption) return { __md: `${children}\n*${caption}*\n` };
        return { __md: children };
      }
      case 'Image': {
        const src = props?.src || '';
        const alt = (props?.alt || 'image').substring(0, 120);
        const fullSrc = src.startsWith('/') ? BASE_URL + src : src;
        return { __md: `\n![${alt}](${fullSrc})\n` };
      }
      default: {
        if (props?.src) {
          const src = props.src;
          const alt = (props?.alt || 'image').substring(0, 120);
          const fullSrc = typeof src === 'string' && src.startsWith('/') ? BASE_URL + src : src;
          const caption = props?.caption || '';
          let md = `\n![${alt}](${fullSrc})\n`;
          if (caption) md += `*${caption}*\n`;
          return { __md: md };
        }
        if (props?.caption && children) {
          return { __md: `${children}\n*${props.caption}*\n` };
        }
        return { __md: children || '' };
      }
    }
  }

  function jsxs(type, props) {
    return jsx(type, props);
  }

  function flattenCell(text) {
    return text.replace(/\n+/g, ' ').replace(/\s+/g, ' ').trim();
  }

  const Fragment = '__fragment__';
  return { jsx, jsxs, Fragment };
}

function codeToMarkdown(code, title) {
  const runtime = createMockRuntime();

  try {
    const fn = new Function('runtime', `
      var _jsx_runtime = {
        jsx: runtime.jsx,
        jsxs: runtime.jsxs,
        Fragment: runtime.Fragment
      };
      ${code}
      return Component;
    `);

    const mod = fn(runtime);

    if (mod && mod.default) {
      const components = {};
      const tagNames = ['h1','h2','h3','h4','h5','p','em','strong','code','pre','a','br','hr',
                        'ul','ol','li','blockquote','table','thead','tbody','tr','th','td',
                        'img','span','div','sup','sub',
                        'math','semantics','mrow','mn','mo','mi','msup','msub','mfrac','mtext','annotation'];
      for (const tag of tagNames) {
        components[tag] = tag;
      }
      components.Figure = 'Figure';
      components.Image = 'Image';

      const result = mod.default({ components });

      let md = '';
      if (result && '__md' in result) {
        md = result.__md;
      } else if (typeof result === 'string') {
        md = result;
      }

      if (title && !md.trimStart().startsWith('# ')) {
        md = `# ${title}\n${md}`;
      }

      md = md.replace(/\n{3,}/g, '\n\n');
      md = md.replace(/\n#{1,6}\s*\n/g, '\n');
      md = md.replace(/\$\s*\$/g, '');

      return md.trim();
    }
  } catch (err) {
    console.error(`  Error evaluating code: ${err.message}`);
    return regexFallback(code, title);
  }

  return regexFallback(code, title);
}

function regexFallback(code, title) {
  const parts = [];
  if (title) parts.push(`# ${title}\n`);

  const matches = code.matchAll(/children:\s*"([^"]+)"/g);
  for (const m of matches) {
    if (m[1].length > 3) parts.push(m[1]);
  }

  return parts.join('\n\n');
}

// Main
const files = readdirSync(RAW_DIR).filter(f => f.endsWith('.json')).sort();
let success = 0;
let failed = 0;

for (const file of files) {
  const jsonPath = join(RAW_DIR, file);
  const mdFile = file.replace('.json', '.md');
  const mdPath = join(OUT_DIR, mdFile);

  console.log(`Converting ${file}...`);

  try {
    const data = JSON.parse(readFileSync(jsonPath, 'utf-8'));
    const props = data.pageProps || {};
    const title = props.title || file.replace('.json', '').replace(/^\d+-/, '').replace(/-/g, ' ');
    const code = props.code || '';

    if (!code) {
      console.log(`  SKIP: no code content`);
      failed++;
      continue;
    }

    const md = codeToMarkdown(code, title);
    writeFileSync(mdPath, md, 'utf-8');
    console.log(`  OK -> ${mdFile} (${md.length} chars)`);
    success++;
  } catch (err) {
    console.error(`  FAILED: ${err.message}`);
    failed++;
  }
}

console.log(`\nDone! ${success} converted, ${failed} failed out of ${files.length} total.`);
