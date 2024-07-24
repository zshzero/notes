- Common ways to iterate
	-  `foreach(var i in _items){}`
	- `for(var i=0; i < CollectionMarshal.AsSpan(_items).lenght; i++){}`
- linq foreach is the worst performing iterator
	- `_items.ForEach(x => {})`
- parallel foreach and parallel linq is faster for bigger lists
	- `Parellel.ForEach(_items, x => {})`
	- `_items.AsParallel().ForAll(x => {})`
- Get a span out of a list is the fastest way
	- `foreach(var i in CollectionMarshal.AsSpan(_items)){}`
	- `for(var i=0; i < CollectionMarshal.AsSpan(_items).length; i++){}`
		- Note : Data shouldn't be added or deleted wile span is in use
- Using Span reference (Just for educational purpose)
```C#
Span<int> asSpan = _items;  
ref var searchSpace = ref MemoryMarshal.GetReference(asSpan);  
for (var i = 9; i < asSpan.Length; i++)  
{  
	var item = Unsafe.Add(ref searchSpace, i);  
	//DoSomething  
}  
return _items;
```
