class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Create a set to keep track of all days when meetings are scheduled
        meeting_days = set()
        
        # Add all days covered by meetings into the set
        for start, end in meetings:
            meeting_days.update(range(start, end + 1))
        
        # Total available days minus days with meetings
        return days - len(meeting_days)