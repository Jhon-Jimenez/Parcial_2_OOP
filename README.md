# Partial 2 - OOP
Repository for partial 2 - Object Oriented Programming

- Name: Jhon Janner Jimenez Zuleta
- Instructor: Jose D. Posada Aguilar

# From problem definition to Implementation

The goal is that with a definition of the problem, propose a UML and implement the solution in Python.

## Problem Statement

## Parking Lot

### Goal

You have a parking lot that accepts cars only during certain times. The cars can be charged by minute, hour or days. You will charge different depending on whether the car is a compact, SUV or a Van. You need to keep track of the available spaces to admit a car. You need to show how many spaces are left. There are different spaces for compact cars, SUV and van. You need to allow multiple users. The users should be able to register and have an account that gives them the ability to reserve a parking spot for the next day.

## UML Diagram

This UML simple diagram below allows a user to sell as many tickets as it wants and to keep track of available seats in the theater. The code for the diagram is in the `parking_lot_uml.puml` file.

![UML Diagram](https://github.com/Jhon-Jimenez/Parcial_2_OOP/blob/main/parkin_lot_uml.png)

Explicación: Para el uml se consideraron las clases necesarias para resolver el problema. Se muestra la creación de una clase abstracta con los atributos y metodos que utilizaran todos los usuarios que se registren por medio de la clase Usuario. Esta clase Usuario hereda de la clase abstracte ABC_Usuario. Una clase parqueadero con cada espacio para los vehiculos. Y una clase para los vehiculos con los metodos y atributos necesario para este problema. Para este problema también se considera el uso de la herencia y la composicion

## Python Code

A simple Python implementation using classes, objects and sustrations.

To test the new code please run `code_to_run.py`