//thunks
export const editRecipeThunk = ({formData,recipeId}) => async (dispatch) => {
    const responseRecipe = await fetch(`/api/recipes/edit/${recipeId}`, {
        method: 'POST',
        body: formData

    });


    if (responseRecipe.ok) {
        const data = await responseRecipe.json();
        // dispatch()
        return data;
    } else if (responseRecipe.status < 500) {
        const data = await responseRecipe.json();
        if (data.errors) {
            return data;
        }
    } else {
        return ['An error occurred. Please try again.']
    }
}