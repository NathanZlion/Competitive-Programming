class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        adjList = defaultdict(list)
        indegree = defaultdict(int)

        for index, recipe in enumerate(recipes):
            for ingredient in ingredients[index]:
                adjList[ingredient].append(recipe)

            indegree[recipe] += len(ingredients[index])
        
        recipesSet = set(recipes)
        
        queue = deque()
        for supply in supplies:
            queue.append(supply)

        resultingRecipes = []
        while queue:
            currRecipe = queue.popleft()
            if (currRecipe in recipesSet):
                resultingRecipes.append(currRecipe)
            
            for recipe in adjList[currRecipe]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)
        
        return resultingRecipes
                    
                
                
            
            
            
                
                
                    
                    
                
                
