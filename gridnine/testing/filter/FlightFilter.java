package com.gridnine.testing.filter;

import com.gridnine.testing.flying.Flight;

import java.time.LocalDateTime;
import java.util.List;

public interface FlightFilter {
    List<Flight> departureBeforeCurrentTime(List<Flight> flights, LocalDateTime currentTime);

    List<Flight> arrivalBeforeDeparture(List<Flight> flights);

    List<Flight> groundTimeMoreThanTwoHours(List<Flight> flights);

}
