def merge_intervals(intervals):
  """
  Merge overlapping intervals.

  Parameters:
    intervals (list): A list of intervals.

  Returns:
    list: A list of merged intervals.
  """

  # Sort the intervals by their start times.
  intervals.sort(key=lambda x: x[0])

  # Initialize the merged intervals list.
  merged_intervals = []

  # Iterate over the intervals.
  for interval in intervals:
    # If the merged intervals list is empty or the current interval does not overlap with the last interval in the list, add the current interval to the list.
    if not merged_intervals or merged_intervals[-1][1] < interval[0]:
      merged_intervals.append(interval)
    # Otherwise, merge the current interval with the last interval in the list.
    else:
      merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

  # Return the merged intervals list.
  return merged_intervals
