import React, { Component } from 'react'

class Repo extends Component {
    title: string | undefined;
    html_url: string | undefined;

    constructor(title?: string, html_url?: string) {
        super(Repo);
        this.title = title;
        this.html_url = html_url;
    }
    getDescription(): string {
        return "This repo " + this.title + " is located at" + this.html_url + " now";
    }

    static fromJSON(d: Object): Repo {
        var o = Object.assign(new Repo(), d);
        return o;
    }

    render() {
        return (
            <div>
                {this.title}
            </div>
        )
    }
}

export default Repo