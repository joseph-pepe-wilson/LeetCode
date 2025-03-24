class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Sort meetings based on start day
        meetings.sort()
        
        # Merge overlapping intervals
        merged_intervals = []
        for start, end in meetings:
            if not merged_intervals or merged_intervals[-1][1] < start:
                merged_intervals.append([start, end])
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
        
        # Calculate the total number of days covered by meetings
        meeting_days = 0
        for start, end in merged_intervals:
            meeting_days += (end - start + 1)
        
        # Subtract meeting days from total available days
        return days - meeting_days