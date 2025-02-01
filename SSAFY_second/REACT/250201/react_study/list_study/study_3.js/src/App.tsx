import React, { JSX } from 'react';
import { Recipe as RecipeType } from './types';
import { recipes } from './data';

interface RecipeProps {
  id: string;
  name: string;
  ingredients: string[];
}

export default function RecipeList(): JSX.Element {
  return (
    <div>
      <h1>Recipes</h1>
      {recipes.map((recipe: RecipeType) => (
        <Recipe key={recipe.id} {...recipe} />
      ))}
    </div>
  );
}

function Recipe({ id, name, ingredients }: RecipeProps): JSX.Element {
  return (
    <div>
      <h2>{name}</h2>
      <ul>
        {ingredients.map((ingredient: string) => (
          <li key={ingredient}>
            {ingredient}
          </li>
        ))}
      </ul>
    </div>
  );
}
