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
       
--接口调用
declare
  v_flag    varchar2(1);
  v_message varchar2(1000);
begin
  l_pos_survival.proc_matu_idvl(p_policy_no => '0066202060007702',
                                p_prod_seq  => 1,
                                p_proc_date => sysdate,
                                p_flag      => v_flag,
                                p_message   => v_message);
end;

declare
  v_product_sur_amt     number;
  v_product_div_sur_amt number;
  v_flag                varchar2(10);
  v_message             varchar2(1000);
begin
  l_pos_pub.calc_product_cash_value(p_policy_no       => '000000033752524',
                                    p_prod_seq        => 1,
                                    p_calc_date       => sysdate,
                                    p_base_cash_value => v_product_sur_amt,
                                    p_div_cash_value  => v_product_div_sur_amt,
                                    p_flag            => v_flag,
                                    p_message         => v_message);
  dbms_output.put_line(v_product_sur_amt || ':' || v_product_div_sur_amt);                                    

end;

declare

  v_flag    varchar2(1000);

  v_message varchar2(1000);

begin

  l_pos_survival.draw_survival_due_idvl('000000033757960',

                                        2,

                                        date '2023-7-31',

                                        date '2023-8-31',

                                        v_flag,

                                        v_message);

  dbms_output.put_line(v_flag || ':' || v_message);                                       

end;

declare

  v_flag    varchar2(1000);

  v_message varchar2(1000);

begin

  l_pos_survival.prepare_to_pay_single(p_policy_no       => '000000033757960',

                                       p_prod_seq        => 1,

                                       p_calc_start_date => date'2023-7-31' - 30,

                                       p_calc_end_date   => date'2023-8-31',

                                       p_flag            => v_flag,

                                       p_message         => v_message);

  dbms_output.put_line(v_flag || ':' || v_message);                                        

end;
