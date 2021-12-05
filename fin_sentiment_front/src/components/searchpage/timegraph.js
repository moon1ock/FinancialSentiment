import React, {useEffect, useState} from 'react'
import { TimeSeries } from "pondjs";
import { Charts, ChartContainer, ChartRow, YAxis, LineChart } from "react-timeseries-charts";

const TimeGraph = (props) =>{
    const {pricematrix} = props;
    const [series, setSeries] = useState(null);
    useEffect(()=>{
        const data = {
            columns: ["time", "value"],
            points: pricematrix
        };
        if(pricematrix){
            setSeries(new TimeSeries(data))
        }
    },[pricematrix])
    return(
        <React.Fragment>
            {series?
                <ChartContainer timeRange={series.timerange()} width={330} format="">
                    <ChartRow height={100}>
                        <YAxis id="axis1" format="$.2f" width="60" type="linear" min={series.min()} max={series.max()}/>
                        <Charts>
                            <LineChart axis="axis1" series={series}/>
                        </Charts>
                    </ChartRow>
                </ChartContainer>:null
            }
        </React.Fragment>
    )
}
export default TimeGraph