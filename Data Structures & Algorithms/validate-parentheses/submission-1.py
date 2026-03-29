class Solution:
    def isValid(self, s: str) -> bool:
        valid_br = ["[]","{}","()"]
        order = []
        for br in s:
            if br in "([{":
                order.append(br)
            else:
                if order:
                    complete_br = order.pop()+ br
                    if complete_br not in valid_br:
                        return False
                else:
                    return False
        if order:
            return False
        return True