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


  Scenario: Update user work experience
    Given que estoy registrado con nombre "Juan", apellido "Gomez", ubicaciones "Buenos Aires, Argentina" y email "jgomez@gmail.com"

    When actualizo mis experiencia laboral a trabajo en "Mercado Libre" como "SR Data scientist" desde "2022-02-01"

    And actualizo mis experiencia laboral a trabaje en "Despegar" como "Data scientist" desde "2021-02-01" hasta "2022-02-01"

    And confirmo la actualizacion

    Then se me informa que se actualizo exitosamente

    And puedo ver que mis dos experiencias cargadas


  Scenario: Update user education
    Given que estoy registrado con nombre "Juan", apellido "Gomez", ubicaciones "Buenos Aires, Argentina" y email "jgomez@gmail.com"

    When actualizo mi educacion a que estudie en el colegio "San jose" bachiller en sociales desde "2001-02-01" hasta "2018-02-01"

    And actualizo mi educacion a que estudio en la "UBA" ingenieria en informatica desde "2019-02-01"

    And confirmo la actualizacion

    Then se me informa que se actualizo exitosamente

    And puedo ver que mi educacion

  Scenario: Follow user
    Given que esta registrado el usuario con nombre "Lucas", apellido "Gomez", ubicaciones "Buenos Aires, Argentina" y email "jgomez@gmail.com"

    And que esta registrado el usuario con nombre "Matias", apellido "Diaz", ubicaciones "Buenos Aires, Argentina" y email "pdiaz@gmail.com"

    When "Lucas" sigue a "Matias"

    Then "Lucas" aparace entre los seguidos de "Matias"

    And "Lucas" tiene entre sus seguidos a "Matias"
