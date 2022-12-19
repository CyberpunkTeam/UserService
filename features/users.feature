Feature: CRUD User


  Scenario: Create user
    Given que no estoy registrado

    When completo el registro, con nombre "Juan", apellido "Gomez", ubicaciones "Buenos Aires, Argentina" y email "jgomez@gmail.com"

    And confirmo el registro

    Then se me informa que se registro exitosamente

  Scenario: Update user
    Given que estoy registrado con nombre "Juan", apellido "Gomez", ubicaciones "Buenos Aires, Argentina" y email "jgomez@gmail.com"

    When actualizo mis datos a nombre "Juan Pablo", apellido "Diaz", ubicaciones "CABA, Argentina"

    And confirmo la actualizacion

    Then se me informa que se actualizo exitosamente

    And puedo ver que mi datos se actualizaron a nombre "Juan Pablo", apellido "Diaz", ubicaciones "CABA, Argentina"
