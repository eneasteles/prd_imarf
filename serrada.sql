
--select * from view_serrada where jogo_fio_id = 76
--select * from producao_serrada where jogo_fio_id = 76
-- lancamentos serrada 68, 80
select 
	ser.serrada,
    maq.maquina,
	maq.lacada,
    blo.bloco,
    mat.material,
	mat.dureza,
    chp.comprimento,
    chp.altura,
    chp.largura,
	chp.espessura_id*100 as espessura,
    date_part('year'::text, ser.data_inicial) AS ano,
    date_part('month'::text, ser.data_inicial) AS mes,
    round(chp.qtde_fios::numeric * chp.comprimento * chp.altura, 3) AS prd_fio_m2,
	round(chp.quantidade::numeric * chp.comprimento * chp.altura * chp.espessura_id, 3) AS m3_chapas_produzidas,
	fio.valor_metro_fio,
	liga.liga,
	fc.fator fator_conversao,
	fio.espessura_fio,
	fio.quantidade_fio,
	fio.comprimento_fio,
	fio.garantia,
    fio.quantidade_fio::double precision * fio.comprimento_fio * fio.garantia AS garantia_fio,
    fio.quantidade_fio::double precision * fio.comprimento_fio * fio.valor_metro_fio / (fio.quantidade_fio::double precision * fio.comprimento_fio * fio.garantia) AS custo_fio_por_m2,
	chp.qtde_fios::double precision * fio.comprimento_fio * fio.valor_metro_fio / (fio.quantidade_fio::double precision * fio.comprimento_fio * fio.garantia) AS custo_fio_por_m2_aplicado,
    ser.data_inicial,
    ser.data_final,
    ser.horimetro_inicial,
    ser.horimetro_final,
    ser.amperagem_max,
    ser.espessura_fio_inicial,
    ser.espessura_fio_final,
    chp.qtde_fios as qtde_fios_aplicado,
    ser.observacoes,
    ser.periferica,
    ser.cala,
	ser.consumo_kwh_fp,
    ser.consumo_kwh_p,
    ser.jogo_fio_id,
( SELECT sum(chp.quantidade) AS sum
           FROM producao_chapas_produzidas chp
          WHERE chp.serrada_id = ser.id) AS qtde_chapas,
fio.quantidade_fio::double precision * fio.comprimento_fio * fio.garantia AS garantia_fio,
    fio.quantidade_fio::double precision * fio.comprimento_fio * fio.valor_metro_fio / (fio.quantidade_fio::double precision * fio.comprimento_fio * fio.garantia) AS custo_fio_por_m2,
	chp.qtde_fios::double precision * fio.comprimento_fio * fio.valor_metro_fio / (fio.quantidade_fio::double precision * fio.comprimento_fio * fio.garantia) AS custo_fio_por_m2_aplicado,
(select vcm3.custo_m3 from view_custo_m3 vcm3 where vcm3.pedreira_id = mat.pedreira_id and 
  			vcm3.ano=date_part('year'::text, ser.data_inicial) and
  			vcm3.mes=date_part('month'::text, ser.data_inicial)) valor_m3, 
    (( SELECT sum(bi.valor) AS sum
           FROM producao_blocoitem bi
          WHERE bi.bloco_id = chp.bloco_id)) / (chp.qtde_fios::numeric * chp.comprimento * chp.altura)::double precision AS custo_m2,
	(select vcm3.custo_m3 from view_custo_m3 vcm3 where vcm3.pedreira_id = mat.pedreira_id and 
  			vcm3.ano=date_part('year'::text, ser.data_inicial) and
  			vcm3.mes=date_part('month'::text, ser.data_inicial))*(blo.comprimento * blo.altura * blo.largura) valor_do_bloco,
    ( SELECT sum(bi.valor) AS sum
           FROM producao_blocoitem bi
          WHERE bi.bloco_id = chp.bloco_id) AS custo_bloco,
		(select vcm3.custo_m3 from view_custo_m3 vcm3 where vcm3.pedreira_id = mat.pedreira_id and 
  			vcm3.ano=date_part('year'::text, ser.data_inicial) and
  			vcm3.mes=date_part('month'::text, ser.data_inicial))*(blo.comprimento * blo.altura * blo.largura)/(chp.comprimento * chp.altura * chp.quantidade) custo_m2_com_borda,
	(select vcm3.custo_m3 from view_custo_m3 vcm3 where vcm3.pedreira_id = mat.pedreira_id and 
  			vcm3.ano=date_part('year'::text, ser.data_inicial) and
  			vcm3.mes=date_part('month'::text, ser.data_inicial))*(blo.comprimento * blo.altura * blo.largura)/((chp.comprimento-0.10) * (chp.altura-0.10) * chp.quantidade) custo_m2_sem_borda,
--			fp.folha,
	mat.pedreira_id, 
	mat.id
--	vcm3.custo_m3

from 						--producao_chapas_produzidas
	producao_serrada ser,
	producao_chapas_produzidas chp,  --bloi 
	producao_maquina maq,
	producao_material mat,
	producao_bloco blo,
	producao_fio_diamantado fio,
	producao_liga liga,
	producao_ligafatorconversao fc
WHERE 
  chp.serrada_id = ser.id AND 
  maq.id = ser.maquina_id AND 
  blo.id = chp.bloco_id AND 
  mat.id = blo.material_id AND
  fio.jogo_fio = ser.jogo_fio_id AND
  liga.id = fio.liga_id AND
  fc.liga_id=liga.id AND
  fc.dureza = mat.dureza
ORDER BY ser.serrada;