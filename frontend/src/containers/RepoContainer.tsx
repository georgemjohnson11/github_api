import React, { Component } from 'react'
import Repo from '../components/Repo'

class RepoContainer extends Component {
    render() {
        return (
            <div>
                {<Repo />}
            </div>
        )
    }
}

export default RepoContainer