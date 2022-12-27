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

  Scenario: Update images user
    Given que estoy registrado con nombre "Juan", apellido "Gomez", ubicaciones "Buenos Aires, Argentina" y email "jgomez@gmail.com"

    When actualizo mis datos a nombre "Juan Pablo", apellido "Diaz", ubicaciones "CABA, Argentina"

    And cambio mi imagen de perfil a "image_1.jpg" y mi imagen de portada a "image_2.jpg"

    And confirmo la actualizacion

    Then se me informa que se actualizo exitosamente

    And puedo ver que mi datos se actualizaron a nombre "Juan Pablo", apellido "Diaz", ubicaciones "CABA, Argentina"

    And mi imagen es "image_1.jpg" y mi imagen de portada es "image_2.jpg"

  Scenario: Search by user name
    Given que esta registrado el usuario con nombre "Juan", apellido "Gomez", ubicaciones "Buenos Aires, Argentina" y email "jgomez@gmail.com"

    And que esta registrado el usuario con nombre "Pedro", apellido "Diaz", ubicaciones "Buenos Aires, Argentina" y email "pdiaz@gmail.com"

    When busco por "ju"

    Then me retorna como resultado el usuario con nombre "Juan"


  Scenario: Search by user lastname
    Given que esta registrado el usuario con nombre "Juan", apellido "Gomez", ubicaciones "Buenos Aires, Argentina" y email "jgomez@gmail.com"

    And que esta registrado el usuario con nombre "Pedro", apellido "Diaz", ubicaciones "Buenos Aires, Argentina" y email "pdiaz@gmail.com"

    When busco por "di"

    Then me retorna como resultado el usuario con apellido "Diaz"


  Scenario: Search by user lastname and name

    Given que esta registrado el usuario con nombre "Juan", apellido "Gomez", ubicaciones "Buenos Aires, Argentina" y email "jgomez@gmail.com"

    And que esta registrado el usuario con nombre "Pedro", apellido "Diaz", ubicaciones "Buenos Aires, Argentina" y email "pdiaz@gmail.com"

    When busco por "a"

    Then me retorna como resultado el usuario con nombre "Juan"

    And me retorna como resultado el usuario con apellido "Diaz"
