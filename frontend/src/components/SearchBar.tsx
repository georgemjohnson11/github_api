import React, { useState } from 'react';
import axios from 'axios';
import RepoContainer from "../containers/RepoContainer";

type SearchProps = { };
type SearchState = { value: string, errorMessage: string | undefined };
interface HandleNameChangeInterface {
  target: HTMLInputElement;
}

class SearchBar extends React.Component<SearchProps, SearchState> {
  constructor(props :SearchProps) {
    super(props);
    this.state = {value: '', errorMessage: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event: { target: HTMLInputElement; }) {
    this.setState({value: (event.target).value, errorMessage: ''});
  }

  handleSubmit(event: React.FormEvent<HTMLFormElement>) {
      const headers = { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}
      axios.get('${process.env.API_URL}')
      .then((res) => console.log(res.data))
      .catch((err) => console.log(err));
      fetch('${process.env.API_URL}', { headers })
      .then(response => response.json())
      .then(data => console.log(data));
        //     const data = await response.json();
        //
        //     // check for error response
        //     if (!response.ok) {
        //         // get error message from body or default to response statusText
        //         const error = (data && data.message) || response.statusText;
        //         console.error('There was an error!', error);
        //         this.setState({ errorMessage: error.toString() });
        //         return Promise.reject(error);
        //     }
        //     alert('A repo was submitted: ' + this.state.value); //error here
        //     this.setState({ value: data })
        //     event.preventDefault();
        // })
        // .catch(error => {
        //     this.setState({ errorMessage: error.toString() });
        //     console.error('There was an error!', error);
        // });
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Repository:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default SearchBar;