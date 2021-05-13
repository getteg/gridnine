package com.gridnine.testing;

import com.gridnine.testing.filter.Filter;
import com.gridnine.testing.filter.FlightFilter;
import com.gridnine.testing.filter.TestingFlightFilter;
import com.gridnine.testing.flying.Flight;
import com.gridnine.testing.flying.FlightBuilder;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.LocalDateTime;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        List<Flight> flights = FlightBuilder.createFlights();
        Filter.printFilter(flights);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        FlightFilter flightFilter = new TestingFlightFilter();
        while(true) {
            switch (br.readLine()){
                case "1" ->  Filter.printFilter(flightFilter.departureBeforeCurrentTime(flights, LocalDateTime.now()));
                case "2" ->  Filter.printFilter(flightFilter.arrivalBeforeDeparture(flights));
                case "3" ->  Filter.printFilter(flightFilter.groundTimeMoreThanTwoHours(flights));
                case "4" ->  {br.close(); return; }
            }

        }
    }

}