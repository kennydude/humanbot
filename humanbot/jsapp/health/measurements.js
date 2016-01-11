import React from 'react';
import request from 'superagent';
import {Link} from 'react-router';
import ErrorView from 'core/error';
import LoadingView from 'core/loading';
import moment from 'moment';
import {Line} from 'react-chartjs';

class MeasurmentItem extends React.Component{
    render(){
        let m = this.props.measurement;
        return (
            <div className="list-item">
                <strong>{parseFloat(m.value)}</strong>&nbsp;
                {m.what}&nbsp;
                {moment(m.created).fromNow()}
            </div>
        )
    }
}

class MeasurementList extends React.Component{
    constructor(){
        super()
        this.state = {
            measurements: [],
            error: null,
            loading: true
        }
    }

    render(){
        if(this.state.error){
            return <ErrorView/>;
        }
        if(this.state.loading){
            return <LoadingView/>;
        }
        let list = this.state.measurements.map((measurement) => {
            return <MeasurmentItem key={measurement.id}
                measurement={measurement} />
        });
        let data = {
            labels: this.state.measurements.map(function(item){
                return moment(item.created).format("YYYY-MM-DD");
            }).reverse(),
            datasets: [
                {
                    label: "Data",
                    data: this.state.measurements.map(function(item){
                        return item.normalised_value;
                    }).reverse()
                }
            ]
        };
        let options = {
            responsive: true,
            scaleBeginAtZero: true
        }

        return (
            <div>
                <div className="heading">
                    Measurements
                </div>
                <Line data={data} width="600" height="200" options={options} />
                {list}
            </div>
        )
    }

    componentDidMount(){
        request.get("/api/humans/" + this.props.params.human_id +
                "/measurements?measurement_for=" + this.props.params.for_id,
                (error, res) => {
            this.setState({
                measurements: res.body['results'],
                error: error,
                loading: false
            });
        });
    }
}

export default MeasurementList;
