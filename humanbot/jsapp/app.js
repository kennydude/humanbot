/*
humanbot jsapp
*/
import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, IndexRoute, Link, browserHistory } from 'react-router';
import HumanPicker from 'core/humanpicker';
import ForList from 'health/fors';
import MeasurementList from 'health/measurements';


class App extends React.Component {
    render(){
        return (<div>
            <div className="header">
                    <div className="logo">
                        humanbot
                    </div>
            </div>
            <div className="content">
                {this.props.children}
            </div>
        </div>)
    }
}

class NoMatch extends React.Component {
    render(){
        return (<div>
            <h1>Not found</h1>
            <p>Page not found</p>
        </div>)
    }
}

class HumanChrome extends React.Component {
    render(){
        return (
            <div>
                <div className="header">
                    <Link to={`/humans/${this.props.params.human_id}/health`}
                            className="icon" activeClassName="active">
                        <img src="/static/icons/ruler.svg" />
                    </Link>
                    <Link to={`/humans/${this.props.params.human_id}/food`}
                            className="icon" activeClassName="active">
                        <img src="/static/icons/food.svg" />
                    </Link>
                </div>
                {this.props.children}
            </div>
        )
    }
}

ReactDOM.render(
  (
      <Router history={browserHistory}>
        <Route path="/" component={App}>
            <IndexRoute component={HumanPicker}/>
            <Route path="/humans/:human_id" component={HumanChrome}>
                <Route path="health">
                    <IndexRoute component={ForList} />
                    <Route path="fors/:for_id" component={MeasurementList} />
                </Route>
                <Route path="*" component={NoMatch}/>
            </Route>
            <Route path="*" component={NoMatch}/>
        </Route>
      </Router>
  ),
  document.getElementById("container")
);
