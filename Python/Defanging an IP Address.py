class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result = []
        address = address.split(".")
        for i in range(len(address)):
            result.append(address[i])
            if i == len(address) - 1:
                return "".join(result)
            result.append("[.]")
        return "".join(result)
