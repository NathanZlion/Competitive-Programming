class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        # use the recipesFromIngredient to represent the graph
        recipesFromIngredient = defaultdict(list)
        # track the indegree of all recipes
        indegree = defaultdict(int)

        for index, recipe in enumerate(recipes):
            for ingredient in ingredients[index]:
                recipesFromIngredient[ingredient].append(recipe)

            indegree[recipe] = len(ingredients[index])

        recipesSet = set(recipes)

        queue = deque()
        for supply in supplies:
            queue.append(supply)

        resultingRecipes = []

        while queue:
            currRecipe = queue.popleft()

            for recipe in recipesFromIngredient[currRecipe]:
                indegree[recipe] -= 1

                if indegree[recipe] == 0:
                    if (recipe in recipesSet):
                        resultingRecipes.append(recipe)

                    queue.append(recipe)


        return resultingRecipes

