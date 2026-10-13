from aoc import read_lines


def build_ingredient_map(data: list[str]) -> dict[str, dict[str, int]]:
    ingredients = {}

    for line in data:
        name, stats = line.split(":")

        ingredient_stats = {}

        for part in stats.split(", "):
            stat, value = part.split()
            ingredient_stats[stat] = int(value)

        ingredients[name] = ingredient_stats

    return ingredients


def build_recipes(
    ingredients: list[str],
    teaspoons_remaining: int,
    recipe: dict[str, int],
    recipes: list[dict[str, int]],
    index=0,
) -> None:
    ingredient = ingredients[index]

    if index == len(ingredients) - 1:
        recipe[ingredient] = teaspoons_remaining
        recipes.append(recipe.copy())
        return

    for amount in range(teaspoons_remaining + 1):
        recipe[ingredient] = amount

        build_recipes(
            ingredients,
            teaspoons_remaining - amount,
            recipe,
            recipes,
            index + 1,
        )


def get_recipe_score(
    recipe: dict[str, int], ingredient_map: dict[str, dict[str, int]]
) -> int:
    totals = {
        "capacity": 0,
        "durability": 0,
        "flavor": 0,
        "texture": 0,
    }

    for ingredient, amount in recipe.items():
        stats = ingredient_map[ingredient]

        for stat in totals:
            totals[stat] += stats[stat] * amount

    score = 1

    for total in totals.values():
        score *= max(0, total)

    return score


def get_calories(
    recipe: dict[str, int], ingredient_map: dict[str, dict[str, int]]
) -> int:
    return sum(
        ingredient_map[ingredient]["calories"] * amount
        for ingredient, amount in recipe.items()
    )


def main():
    data = read_lines(__file__)

    ingredient_map = build_ingredient_map(data)

    recipes = []

    build_recipes(list(ingredient_map.keys()), 100, {}, recipes)

    best_recipe = None
    best_score = 0

    for recipe in recipes:
        if get_calories(recipe, ingredient_map) != 500:
            continue

        score = get_recipe_score(recipe, ingredient_map)

        if score > best_score:
            best_score = score
            best_recipe = recipe

    print(best_recipe)
    print(best_score)


if __name__ == "__main__":
    main()
