class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        num_of_people = len(people)
        number_of_skills = len(req_skills)

        skill_hash = {skill: index for index, skill in enumerate(req_skills)}
        skills_mask_of_person = [0] * num_of_people

        for i in range(num_of_people):
            for skill in people[i]:
                skills_mask_of_person[i] |= 1 << skill_hash[skill]

        dp = [(1 << num_of_people) - 1] * (1 << number_of_skills)
        dp[0] = 0
        for skills_mask in range(1, 1 << number_of_skills):
            for i in range(num_of_people):
                smaller_skills_mask = skills_mask & ~skills_mask_of_person[i]
                if smaller_skills_mask != skills_mask:
                    people_mask = dp[smaller_skills_mask] | (1 << i)
                    if people_mask.bit_count() < dp[skills_mask].bit_count():
                        dp[skills_mask] = people_mask

        req_skill_mask = 2**number_of_skills-1
        answer_mask = dp[req_skill_mask]
        res = []
        for i in range(num_of_people):
            if (answer_mask >> i) & 1:
                res.append(i)

        return res