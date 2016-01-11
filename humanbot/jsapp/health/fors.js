import React from 'react';
import request from 'superagent';
import {Link} from 'react-router';
import ErrorView from 'core/error';

class For extends React.Component {
    render(){
        let human = this.props.human;
        return (
            <Link className="list-item" to={`/humans/${human}/health/fors/${this.props.for.id}`}>
                {this.props.for.name}
            </Link>
        )
    }
}

class ForList extends React.Component{
    constructor(){
        super()
        this.state = {
            fors: [],
            error: null
        }
    }

    render(){
        if(this.state.error){
            return <ErrorView/>;
        }
        let list = this.state.fors.map((f) => {
            return <For key={f.id} for={f} human={this.props.params.human_id} />
        });
        return (
            <div>
                <div className="heading">
                    Measurements
                </div>
                {list}
            </div>
        )
    }

    componentDidMount(){
        request.get("/api/humans/" + this.props.params.human_id +
                "/measurements/for", (error, res) => {
            this.setState({
                fors: res.body['results'],
                error: error
            });
        });
    }
}

export default ForList;
