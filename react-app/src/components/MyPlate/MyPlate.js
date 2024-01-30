import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import DeleteRecipeFormModal from "../DeleteRecipeFormModal"
import defaultPhoto from '../Profile/profileDefaultPhoto.png'
import "./MyPlate.css";

function MyPlate() {
	const [createdRecipes, setCreatedRecipes] = useState([]);
	const [likedRecipes, setLikedRecipes] = useState([]);

	const sessionUser = useSelector((state) => state.session.user);
	const userId = sessionUser.id;
    const readDate = new Date(sessionUser.time_created).toDateString();

	useEffect(() => {
		async function fetchData() {
			const response = await fetch(`/api/recipes/my_plate/${userId}`);
			const responseData = await response.json();
			setCreatedRecipes(responseData.created);
			setLikedRecipes(responseData.liked);
		}
		fetchData();
	}, [userId]);

	const likedRecipeBlock = likedRecipes.map((recipe) => {
		return (
			<NavLink key={`likedLink'_${recipe.id}`} to={`/recipes/${recipe.id}`} className="recipeNav">
				<div key={`liked'_${recipe.id}`} className="singleRecipe">
					<img alt={recipe.name} className="recipePic" src={(recipe.medias && recipe.medias[0]) ? recipe.medias[0]['mediaUrl'] : defaultPhoto} />
					<h4 className="recipeTitle">{recipe.title.slice(0, 25) + '...'}</h4>
				    <p className="authorName">by: {recipe.author.username} in {recipe.tags ? recipe.tags[0].name : "All Recipes"}</p>
			    </div>
            </NavLink>
		);
	});

	const createdRecipeBlock = createdRecipes.map((recipe) => {

		return (
			<div key={`createdWrapper'_${recipe.id}`}>
            <NavLink to={`/recipes/${recipe.id}`} className="recipeNav">
					<div key={`created'_${recipe.id}`} className="singleRecipe">
						<img alt={recipe.name} className="recipePic" src={(recipe.medias && recipe.medias[0])? recipe.medias[0]['mediaUrl'] : "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARMAAAC3CAMAAAAGjUrGAAAAKlBMVEXg4OD////j4+Pd3d36+vri4uLw8PDs7Oz29vb09PTa2tr5+fnm5ubx8fF4aKZkAAABUUlEQVR4nO3Z246CMBRAUWjBgQ78/+8OeMVR4E0TzlovJpUY3DnBglUFAAAAAAAAAAAAAAAAAAAAAAAAAMAh5DZtq/K3T/HTclfv6YNFyf1ukro+ffssPyvX9bg9BtMg/cYalKnJz06TU93EazK/tENa+eJRm+Rxump0K0cEbXI6X0q7t189aJN8/X1p3x4Ru8nwWO7uQxO0Sbk2eax2j51a0CbVcNma3UejW2xfozbJqZley22tW+7pozapcinleUruUcI2Wa4sbgrnKLGbpPPC033yFCV0k2ben/x/dNDnwE1yM2/aXp+mlMBN5iR18/qAKW6T85S8FbfJapKwTdanJHCT9SSaaDLT5NWlSWrXpMh7tpW3g97v9CkN61LqwjUZN64lNzv/AB1O2f+/eCz7H3MspeRtJVwSAAAAAAAAAAAAAAAAAAAAAAAAAICj+gOmbQmv8zyqjAAAAABJRU5ErkJggg=="} />
						<h4 className="recipeTitle">{recipe.title.slice(0, 25)+'...'}</h4>
				    <p className="authorName">by: {recipe.author.username} in {recipe.tags ? recipe.tags[0].name : "All Recipes"}</p>

			    </div>
            </NavLink>
			<div key={`createdEdit&DeleteBtn'_${recipe.id}`} style={{display:'flex', justifyContent:'space-around'}}>
			<NavLink
				to={`/recipes/edit/${recipe.id}`} className='btn-category-header'
				style={{ marginTop: '1%' }}
			>Edit</NavLink>
			<DeleteRecipeFormModal
				className='btn-category-header'
			    id={recipe.id}
				userId={userId}
				setCreatedRecipes={setCreatedRecipes}
				setLikedRecipes={setLikedRecipes}
				/>
			</div>
			</div>
		);
	});



	return (
		<div className="plateContainer">
            <div className="plateTop">
                <div className="plateTopCard">
					<img alt={sessionUser.username} src={sessionUser.profilePic ? sessionUser.profilePic :'https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png'} className="profileCircle"/>
                    <div className="profCard">
                        <h2 id="username">{sessionUser.username}</h2>
                        <div className="buttonDiv">
                            <NavLink to={`/users/${sessionUser.id}`} className="profButton">View Profile</NavLink>
                        </div>
                        <p className="joinDate"><i className="fas fa-carrot"></i>Joined {readDate}</p>
                    </div>
                </div>
            </div>
			<div className="recipeBlock">
				<h1 className="plateHeadings">MY RECIPES </h1>
				<ul className="recipeList">{createdRecipeBlock}</ul>
			</div>
			<div className="recipeBlock">
				<h1 className="plateHeadings">RECIPES I LIKE </h1>
				<ul className="recipeList">{likedRecipeBlock}</ul>
			</div>
		</div>
	);
}

export default MyPlate;
