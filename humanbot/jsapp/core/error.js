import React from 'react';

class ErrorView extends React.Component {
    render(){
        return (
            <div className="message">
                Sorry, a technical error occurred which meant this page
                could not be loaded
            </div>
        )
    }
};

export default ErrorView;
