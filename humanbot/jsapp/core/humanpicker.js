import React from 'react';
import request from 'superagent';
import {Link} from 'react-router';
import ErrorView from 'core/error';

/**
Component to display a human object
*/
class Human extends React.Component {
    render(){
        let human = this.props.human;
        return (
            <Link to={`/humans/${human.id}`}>
                <div className="list-item">
                    <img className="avatar" src={human.picture} />
                    {human.name}
                </div>
            </Link>
        )
    }
}

/**
Component to display a list of humans
*/
class HumanPicker extends React.Component{
    constructor() {
        super();
        this.state = { humans: [], error: null };
    }

    render(){
        if(this.state.error){
            return <ErrorView/>;
        }
        let list = this.state.humans.map((human) => {
            return (
                <Human human={human} key={human.id} />
            );
        });
        return (
            <div>
                <div className="heading">
                    Humans
                </div>
                {list}
            </div>
        )
    }

    componentDidMount(){
        request.get("/api/humans", (error, res) => {
            this.setState({
                humans: res.body['results'],
                error: error
            });
        });
    }
}
export default HumanPicker;
