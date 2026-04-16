# Introduction to Intervals

## Intuition

An interval consists of two values: a start point and an end point. It represents a continuous segment on the number line that includes all values between these two points. It is often used to represent a line, time period, or a continuous range of values.

- An interval’s start point indicates where the interval begins.

- An interval’s end point indicates where the interval ends.

![Image represents a simple horizontal timeline diagram illustrating a process or sequence.  The diagram consists of a thi](./images/8b0c580f_image-09-00-1-T6PHXV27.svg)

Intervals can be closed, open, or half-open, based on whether their start or end points are included in the interval.

- **Closed intervals:** Both the start and end points are included in the interval.

![Image represents a line segment with thick, black endpoints and a thick, black line connecting them.  The endpoints are ](./images/23af7d89_image-09-00-2-7GBBXDWD.svg)

- **Open intervals:** The start and end points are not included in the interval.

![The image represents a simple line graph or diagram illustrating a relationship between two data points.  A thick, horiz](./images/b4cff7d1_image-09-00-3-HPLWHZYM.svg)

- **Half-open intervals:** Either the start or the end point is included, while the other is not.

![Image represents two identical line segments, each visually depicting a range.  Both segments are thick, black lines hor](./images/6d39e097_image-09-00-4-LLFNYSUD.svg)

When presented with an interval problem in an interview, It’s important to clarify whether the intervals are open, closed, or half-open, as this can change the nature of how intervals overlap.

**Overlapping intervals**

Two intervals overlap if they share at least one common value.

![Image represents a visual depiction of an overlap between two intervals on a number line.  A light green rectangle label](./images/99f6bad7_image-09-00-5-CQEXEBQA.svg)

The central challenge in most interval problems involves managing overlapping intervals
effectively. Whether identifying or merging overlapping intervals, it’s important
to determine how the overlap between intervals influences the desired outcome of
the problem. The problems in this chapter involve handling overlapping intervals
in varying situations.

**Sorting intervals**

In most interval problems, sorting the intervals before solving the problem is quite helpful since it allows them to be processed in a certain order.

We usually **sort intervals by their start point** so they can be traversed in chronological order. When two or more intervals have the same start point, we might also need to consider each interval’s end points during sorting.

**Separating start and end points**

In certain scenarios, it might be beneficial to process the start and end points of intervals separately. This usually involves creating two sorted arrays: one containing all start points and another containing all end points. For example, this is needed in the sweeping line algorithm, which is explored in the *Largest Overlap of Intervals* problem.

![Image represents a data structure illustrating the concept of intervals.  The top line defines a list named `intervals` ](./images/7c14e379_image-09-00-6-LYZMPB77.svg)

**Interval class definition**

For the problems in this chapter, intervals are represented using the class below.

```python
class Interval:
   def __init__(self, start, end):
       self.start = start
       self.end = end

```

```javascript
class Interval {
  constructor(start, end) {
    this.start = start
    this.end = end
  }
}

```

```java
class Interval {
    int start;
    int end;

    public Interval(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

```

## Real-world Example

**Scheduling systems:** Intervals are widely used in scheduling systems. For instance, in a conference room booking system, each booking is represented as an interval. The interval representation is used if the system requires functionality, such as determining the maximum number of overlapping bookings to ensure sufficient room availability. By analyzing these intervals, the system can efficiently allocate resources and prevent double bookings.

## Chapter Outline

![Image represents a hierarchical diagram illustrating two common coding patterns related to interval management.  A round](./images/01ef110f_image-09-00-7-DR2DBFFY.svg)