package com.gridnine.testing.filter;

import com.gridnine.testing.flying.Flight;

import java.util.List;

public class Filter {

    public static void printFilter(List<Flight> flights) {
        for (Flight flight : flights) {
            System.out.println(flight + "\n*******************");
        }
        System.out.println("Выберите фильтр:\n1 - Исключить вылет до текущего момента времени\n" +
                "2 - Исключить полёты, где имеются сегменты с датой прилёта раньше даты вылета\n" +
                "3 - Исключить полёты, при которых общее время, проведённое на земле превышает два часа\n" +
                "4 - выход");
    }
}
