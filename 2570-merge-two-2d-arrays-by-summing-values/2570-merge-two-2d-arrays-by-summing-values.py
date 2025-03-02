class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged_dict = {}

        # Add ids and values from nums1 to the dictionary
        for id_val in nums1:
            id, val = id_val
            merged_dict[id] = val

        # Add values from nums2 to the corresponding ids in the dictionary
        for id_val in nums2:
            id, val = id_val
            if id in merged_dict:
                merged_dict[id] += val
            else:
                merged_dict[id] = val

        # Convert the dictionary to a sorted list of lists
        merged_list = [[id, val] for id, val in merged_dict.items()]
        merged_list.sort(key  = lambda x : x[0])

        return merged_list