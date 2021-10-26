import React from 'react';
import { Link } from 'react-router-dom';
import Header from "../components/Header";
import SearchBar from "../components/SearchBar";

const Home = () => (
    <div className='container'>
        <Header />
        <div className='jumbotron mt-5'>
            <h1 className='display-4'>Welcome to the Github API Inquirer!</h1>
            <hr className='my-4' />
            <SearchBar />
        </div>
    </div>
);

export default Home;