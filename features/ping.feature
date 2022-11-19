Feature: ping en la app

  Scenario: ping en la app
     Given la app esta encendida
      When si le pego al /
      Then recibo un mensaje de exito