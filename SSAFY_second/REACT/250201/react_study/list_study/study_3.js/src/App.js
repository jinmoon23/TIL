"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = RecipeList;
var data_js_1 = require("./data.js");
function RecipeList() {
    return (Recipes < /h1>);
    {
        data_js_1.recipes.map(function (recipe) {
            return key;
        }, { recipe: recipe, : .id }, __assign({}, recipe) /  >
        );
    }
    /div>;
    ;
}
function Recipe(_a) {
    var id = _a.id, name = _a.name, ingredients = _a.ingredients;
    return key = { id: id } >
        { name: name } < (/h2>);
    {
        ingredients.map(function (ingredient) {
            return key;
        }, { ingredient: ingredient } >
            { ingredient: ingredient }
            < /li>);
    }
    /ul>
        < /div>;
}
