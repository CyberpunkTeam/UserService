Feature: CRUD User


  Scenario: Create user
    Given que no estoy registrado

    When completo el registro, con nombre "Juan", apellido "Gomez", ubicaciones "Buenos Aires, Argentina" y email "jgomez@gmail.com"

    And confirmo el registro

    Then se me informa que se registro exitosamente
