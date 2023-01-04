class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        splittedDomain = []
        for domain in cpdomains:
            splittedDomain.append(domain.split())
        
        cp = defaultdict(int)

        for domain in splittedDomain:
            subDomain = domain[1].split('.')
            for i in range(len(subDomain)):
                cp[".".join(subDomain[i:])] += int(domain[0])
            
        cpDomainsRes = []
        for domain in cp:
            res = str(cp[domain]) + " " + domain
            cpDomainsRes.append(res)            
        
        return cpDomainsRes

