class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort the list of people based on decreasing height
        # Using python's insert function, loop through people and insert the 
        # person with the index of number of people in front of them
        # this will ensure the shorter people with same number of people taller 
        # in front of them will come first since the insert function overwrites them to 
        # that index, and pushes everyone back
        if not people:
            return []

        people = sorted(people, key=lambda x: (-x[0], x[1]))
        
        result = []
        
        for person in people:
            result.insert(person[1], person)
        
 
        return result