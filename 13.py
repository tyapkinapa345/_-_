INSERT INTO customers (first_name, last_name, email, phone, registration_date)
SELECT
    first_name,
    last_name,
    -- уникальный email: имя.фамилия + случайное число + домен
    lower(first_name) || '.' || lower(last_name) || floor(random() * 10000)::text || '@' ||
    (array['gmail.com', 'yandex.ru', 'mail.ru', 'example.com', 'bk.ru'])[floor(random()*5)+1] AS email,
    -- телефон в формате +7 XXX XXX-XX-XX
    '+7 ' || (100 + floor(random()*900))::text || ' ' ||
    (100 + floor(random()*900))::text || '-' ||
    (10 + floor(random()*90))::text || '-' ||
    (10 + floor(random()*90))::text AS phone,
    -- дата регистрации за последние 3 года
    CURRENT_DATE - (random() * 1095)::int * interval '1 day' AS registration_date
FROM (
    SELECT
        (array['Александр','Алексей','Андрей','Артём','Владимир','Дмитрий','Евгений','Иван','Максим','Михаил','Николай','Павел','Роман','Сергей','Юрий',
                'Анна','Елена','Мария','Ольга','Татьяна','Наталья','Ирина','Светлана','Екатерина','Юлия']) [floor(random()*25)+1] AS first_name,
        (array['Иванов','Смирнов','Кузнецов','Попов','Васильев','Петров','Соколов','Михайлов','Новиков','Фёдоров','Морозов','Волков','Алексеев','Лебедев','Семёнов',
                'Козлов','Михайлова','Новикова','Морозова','Волкова','Алексеева','Лебедева','Семёнова','Егорова','Павлова']) [floor(random()*25)+1] AS last_name
    FROM generate_series(1, 5000)
) AS names
ON CONFLICT (email) DO NOTHING;  -- на случай редкого совпадения email
