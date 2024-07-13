
STORY = {-1: {'message': '<b>Зачин</b> для вашей сказки:'},
         0: {'button': 'Отлучка 🚗', 'msg': '<b>Отлучка</b>\nКто-то уезжает, уходит, оставляет вас в одиночестве.', 'message': '<i>Вы остаётесь одни. Кто-то уезжает, отлучается, уходит. Для кого-то одиночество кажется тягостным, но не для вас. Напротив, в этом состоянии вы находите для себя новые возможности!</i>\n\n<b>Запрет</b>\n<i>Уходя, вам было запрещено. Строгий запрет, буквально табу. Не надо этого делать, нельзя. Будут последствия. Как же вы поступите?\n«Не заходи только в десятую комнату»\n«В этот чулан не заглядывай»\n«Никому не отпирай дверь» и т.д.</i>'},
         1: {'button': 'Вредительство 🐞', 'msg': '<b>Вредительство</b>\nВраг наносит вам или одному из членов вашей семьи вред.', 'message': '<i>Ваш враг делает первый шаг: вредит вам или члену вашей семьи, другу или соратнику. Какой будет ваша реакция? Что сделал этот подлец?</i>\n\n<b>Посредничество</b>\n<i>Кто-то сообщает вам о том, кто ваш враг и что он хочет. Быть может, это повергнет вас в шок. Быть может, обрадует, но ясность все же приходит.</i>\n\n<b>Отправка</b>\n<i>Вы покидаете дом или то место, коим его считаете. Отправляясь в долгий путь, вы берете с собой самое важное и нужно из своих личных качеств или вещей.\nКуда вас заведёт тропа?</i>'},
         2: {'button': 'Недостача 🤔', 'msg': '<b>Недостача</b>\nВам чего-либо не хватает или очень хочется иметь: волшебное средство, диковинку, невесту.', 'message': '<i>Вы понимаете, что вам недостаёт чего-то важного. Как, должно быть, вам хочется этим обладать, завоевать, заполучить! Что это - жених, невеста, драгоценность или способность? Решать вам.</i>\n\n<b>Отправка</b>\n<i>Вы покидаете дом или то место, коим его считаете. Отправляясь в долгий путь, вы берете с собой самое важное и нужно из своих личных качеств или вещей.</i>'},
         3: {'button': 'Нарушить ❌', 'msg': '<b>Нарушение запрета</b>\nВы нарушаете запрет.', 'message': '<i>Вы нарушаете запрет. Конечно, ваша бунтарская суть не позволит вам так просто игнорировать этот соблазн. А последствия... Да к чёрту их!</i>\n\n<b>Описание и появление врага</b>\n<i>А вот и он, ваш враг. Прекрасный или ужасный, но он создан для того, чтобы испортить вам жизнь одним только фактом своего существования. Опишите его. Где он? Что делает? Почему ненавидит вас?</i>\n\n<b>Выведывание</b>\n<i>Ваш враг хочет узнать о вас что-то важное, он делает все, чтобы собрать по крупицам сведения, важные в его борьбе против вас.\n«Стала ведьма вызнавать, выспрашивать»</i>\n\n<b>Выдача</b>\n<i>Вашему врагу даются сведения о вас. Зеркальце: «Но царевна все ж милее...»\nДолго ли, коротко ли, а сведения о вас каким-то образом попали в руки врага. Тот, кто владеет информацией - владеет миром!</i>\n\n <b>Обман </b>\n<i>Враг готовит для вас ловушку: обман, который часто кажется абсолютной правдой. Он принимает чужое обличие, путает слух, льстит, увлекает, колдуя или науськивая других против вас.\nВолк подражает голосу мамы-козы. В ход идет всё — волшебные снадобья, обман, насилие</i>'},
         4: {'button': 'Послушаться ✔️', 'msg': '<b>Послушание</b>\nВы слушаетесь запрета.', 'message': '<i>Вы послушно следуете запрету: не суётесь, куда не стоит, делаете все по правилам. Меньше хлопот после. И вам спокойнее и проще жить!</i>'},
         5: {'button': 'Подчиниться обману 🫡', 'msg': '<b>Подчинение обману</b>\nВы поддаетесь обману и помогаете собственному врагу: царевна ест предложенное старухой яблочко.', 'message': '<i>Вы, ввиду вашего характера или профессии, поддаётесь на обман вашего врага. Идете на поводу, легковерно доверяя себя в руки того, кто хочет вам зла. Ваш враг добился своего. Вы повержены, и на этом ваша история заканчивается</i>'},
         6: {'button': 'Отказ в подчинении🖕', 'msg': '<b>Отказ в подчинении</b>\nВы не поддается обману и не помогаете собственному врагу: козлята отказывают открыть дверь волку.', 'message': '<i>Что-то не так: вы чувствуете это. Всем нутром. И отказываетесь от предложения или действий своего врага, быть может, даже не распознав его, но предчувствуя беду!</i>'},
         7: {'button': 'Продолжить путешествие 🛤', 'msg': 'Быть может, вы хотите продолжить?', 'message': '<i>Вы решаете во что бы то ни стало бороться до конца! В конце концов, надежда умирает последней.</i>\n\n<b>Идентификация врага</b>\n<i>Наконец, всё встает на свои места. Вы понимаете, что вам противоборствуют тайные силы. Пора браться за дело и бороться за своё счастье и даже жизнь!</i>\n\n<b>Решение противодействия врагу</b>\n<i>«Позволь мне, царь, попытать счастья...»\nВы определились: борьба не на жизнь, а на смерть. Да, не сразу, но вы понимаете, что иначе этот конфликт не разрешить!</i>\n\n<b>Отправка</b>\n<i>Вы покидаете дом или то место, коим его считаете. Отправляясь в долгий путь, вы берете с собой самое важное и нужно из своих личных качеств или вещей.</i>'},
         8: {'button': 'Идентификация врага 👤', 'msg': '<b>Идентификация врага</b>\nВы понимаете, что вам противоборствуют тайные силы.', 'message': '<i>Наконец, всё встает на свои места. Вы понимаете, что вам противоборствуют тайные силы. Пора браться на дело и бороться за своё счастье и даже жизнь!</i>\n\n<b>Решение противодействия врагу</b>\n<i>«Позволь мне, царь, попытать счастья...»\nВы определились: борьба не на жизнь, а на смерть. Да, не сразу, но вы понимаете, что иначе этот конфликт не разрешить!</i>\n\n<b>Отправка</b>\n<i>Вы покидаете дом\nВы покидаете дом или то место, коим его считаете. Отправляясь в долгий путь, вы берете с собой самое важное и нужно из своих личных качеств или вещей.</i>'},
         9: {'button': 'Посредничество 🗣', 'msg': '<b>Посредничество</b>\nВам сообщают о беде, о наличии врага.', 'message': '<i>Кто-то сообщает вам о том, кто ваш враг и что он хочет. Быть может, это повергнет вас в шок. Быть может, обрадует, но ясность все же приходит.</i>\n\n<b>Решение противодействия врагу</b>\n<i>«Позволь мне, царь, попытать счастья...»\nВы определились: борьба не на жизнь, а на смерть. Да, не сразу, но вы понимаете, что иначе этот конфликт не разрешить!</i>\n\n<b>Отправка</b>\n<i>Вы покидаете дом или то место, коим его считаете. Отправляясь в долгий путь, вы берете с собой самое важное и нужно из своих личных качеств или вещей.</i>'},
         10: {'button': 'Испытание 🗿', 'msg': '<b>Испытание</b>\nВы проходите любое испытание.', 'message': '<i>Впереди вас ждет настоящее испытание. В сказках обычно это совершение какого-то экстраординарного поступка или действия, а может, пришла пора блеснуть своими интеллектуальными способностями? Кто знает.</i>'},
         11: {'button': 'Нападение 👊', 'msg': '<b>Нападение</b>\nВы подвергаетесь нападению.', 'message': '<i>Вы подвергаетесь внезапному нападению. Кто знает, какие силы сейчас нацелены на вас и какая рука? Одно точно: ваша жизнь в опасности!</i>'},
         12: {'button': 'Услуга 🆘', 'msg': '<b>Услуга</b>\nВы оказываете кому-то услугу.', 'message': '<i>Что-то встает на вашем пути и просит об услуге, которую в ваших силах оказать. В сказках обычно это передача какого-то знания или средства, или действие, подразумевающее безвозмездное оказание помощи.</i>\n\n<b>Перемещение в иное царство</b> — <i>к месту нахождения предмета поисков или средства исцеления.\n«Долго ли, коротко шла Марьюшка, уже три пары башмаков истоптала». Вы летите по воздуху, на волшебном животном или в образе его, на летучем предмете, его ведут — клубочек указывает путь.\nЛокация меняется: вас после ваших испытаний перемещают в другое место, ведь там и избавление от физических мук, и, может быть, цель ваших поисков. Быть может, вы добираетесь до цели самостоятельно?</i>\n\n<b>Враг на пути</b>\n<i>А вот и решающая битва! Ваш враг встречает вам, попадется вам на пути, теперь вы можете открыто ему противостоять. Но станете ли?</i>'},
         13: {'button': 'Служба 🤑', 'msg': '<b>Служба</b>\nВы проходите службу на кого-то.', 'message': '<i>Оказывается, чтобы двинуться дальше, вам необходимо тяжело поработать. Вы оказываетесь на службе у кого-то чрезвычайно важного. Что это будет за служба, на какой срок?</i>'},
         14: {'button': 'Плен 🔐', 'msg': '<b>Плен</b>\nВы вызволяете кого-то из плена.', 'message': '<i>Не оскудеет рука дающего! На пути у вас некто, кто просит помощи вызволения из плена. Помогайте, чем можете!</i>\n\n<b>Получение волшебного средства или помощника</b>\n<i>Вы получаете помощь «Дал старичок Ивану коня», «Только скажи: по щучьему велению, по моему хотению...» Средством может быть животное, предмет, качество\nА вот и награда за ваши труды. Вам помогают! Причем, неважно как - словом, делом, предметом, качеством, животным, чем угодно, но вы не одни!</i>\n\n<b>Враг на пути</b>\n<i>А вот и решающая битва! Ваш враг встречает вам, попадется вам на пути, теперь вы можете открыто ему противостоять. Но станете ли?</i>'},
         15: {'button': 'Киньте кубик! 🎲', 'msg': 'Сделайте выбор! Киньте кости!'},
         16: {'button': 'Перемещение в иное царство 🏰', 'msg': '<b>Перемещение в иное царство</b> — к месту нахождения предмета поисков или средства исцеления.', 'message': '<i>«Долго ли, коротко шла Марьюшка, уже три пары башмаков истоптала». Вы летите по воздуху, на волшебном животном или в образе его, на летучем предмете, его ведут — клубочек указывает путь.\nЛокация меняется: вас после ваших испытаний перемещают в другое место, ведь там и избавление от физических мук, и, может быть, цель ваших поисков. Быть может, вы добираетесь до цели самостоятельно?</i>\n\n<b>Враг на пути</b>\n<i>А вот и решающая битва! Ваш враг встречает вам, попадется вам на пути, теперь вы можете открыто ему противостоять. Но станете ли?</i>'},
         17: {'button': 'Получить помощника 🐾', 'msg': '<b>Получение волшебного средства или помощника.</b>\nВы встречаете встречаете с тем, кто разделяет с вами дорогу', 'message': '<i>Вы получаете помощь «Дал старичок Ивану коня», «Только скажи: по щучьему велению, по моему хотению...» Средством может быть животное, предмет, качество\nА вот и награда за ваши труды. Вам помогают! Причем, неважно как - словом, делом, предметом, качеством, животным, чем угодно, но вы не одни!</i>\n\n<b>Враг на пути</b>\n<i>А вот и решающая битва! Ваш враг встречает вам, попадется вам на пути, теперь вы можете открыто ему противостоять. Но станете ли?</i>'},

         50: {'message': '<b>Вы не прошли испытание. Ваш путь окончен.</b>\n<i>К сожалению, вы проиграли и не прошли испытание. Вы не выдерживаете или покалечены до такой степени, что не можете продолжать эту историю.</i>'},
         51: {'message': '<b>Вы прошли испытание, но получили урон.</b>\n<i>Вы прошли это тяжелое испытание, но получили какой-то урон: отсеченную руку, тотальную слабость. Но вы живы!</i>'},
         52: {'message': '<b>Вы прошли испытание!</b>\n<i>Воистину на небесах вам кто-то помогает! Вы прошли испытание с честью, даже не устав. Время двигаться дальше!</i>\n\n<b>Перемещение в иное царство</b> — <i>к месту нахождения предмета поисков или средства исцеления.\n«Долго ли, коротко шла Марьюшка, уже три пары башмаков истоптала». Вы летите по воздуху, на волшебном животном или в образе его, на летучем предмете, его ведут — клубочек указывает путь.\nЛокация меняется: вас после ваших испытаний перемещают в другое место, ведь там и избавление от физических мук, и, может быть, цель ваших поисков. Быть может, вы добираетесь до цели самостоятельно?</i>\n\n<b>Враг на пути</b>\n<i>А вот и решающая битва! Ваш враг встречает вам, попадется вам на пути, теперь вы можете открыто ему противостоять. Но станете ли?</i>'},
         53: {'message': '<b>Вы не пережили нападение. Ваш путь окончен.</b>\n<i>К сожалению, вы проиграли, и над вами одержали победу. Вы убиты или покалечены до такой степени, что не можете продолжать эту битву.</i>'},
         54: {'message': '<b>Вы пережили нападение, но получили урон.</b>\n<i>Вы прошли это тяжелое испытание, но получили какой-то урон: отсеченную руку, тотальную слабость. Но вы живы!</i>\n\n<b>Перемещение в иное царство</b> — <i>к месту нахождения предмета поисков или средства исцеления.\n«Долго ли, коротко шла Марьюшка, уже три пары башмаков истоптала». Вы летите по воздуху, на волшебном животном или в образе его, на летучем предмете, его ведут — клубочек указывает путь.\nЛокация меняется: вас после ваших испытаний перемещают в другое место, ведь там и избавление от физических мук, и, может быть, цель ваших поисков. Быть может, вы добираетесь до цели самостоятельно?</i>\n\n<b>Враг на пути</b>\n<i>А вот и решающая битва! Ваш враг встречает вам, попадется вам на пути, теперь вы можете открыто ему противостоять. Но станете ли?</i>'},
         55: {'message': '<b>Вы победили!</b>\n<i>Воистину на небесах вам кто-то помогает! Вы победили неприятеля с честью, даже не устав. Время двигаться дальше!</i>'},

         18: {'button': 'Борьба с Врагом 🤼‍♂️', 'msg': '<b>Борьба с Врагом</b>\nВы вступаете в схватку с врагом.', 'message': '<i>Да. Быть битве и теперь только вам решать, станет ли эта битва последней или - одной из многих!</i>'},
         19: {'button': 'Отказ от борьбы с Врагом 🕊', 'msg': '<b>Отказ от борьбы с Врагом</b>\nВы отказываетесь от битвы.', 'message': '<i>Нет, эта битва не про вас. Вы решаете отказаться сражаться с этим мерзким типов. Вы выше этого.</i>'},
         20: {'button': 'Победа героя 🏆', 'msg': '<b>Победа героя</b>\nВы одерживаете победу, которую так заслужили.', 'message': '<i>Вы побеждаете! Фанфары и горны трубят в вашу честь!</i>\n\n<b>Начальная беда или недостача ликвидируется</b>\n<i>А вот и ваш приз: что бы ни было в самом начале, чего бы вы не лишились, что бы ни хотели получить - все это ваше. Ликуйте!</i>'},
         21: {'button': 'Поражение героя: 🥈', 'msg': '<b>Поражение героя</b>\nСуществуют злодеи, которых невозможно победить.', 'message': '<i>К сожалению, вы погибаете в этой неравной схватке. Бывают и такие сказки, правда? Но вы оставили след в этом мире, он станет первым шагов к переменам.</i>'},
         22: {'button': 'Возвращение домой 🏡', 'msg': '<b>Возвращение домой</b>\nВас ждут дома, пора идти.', 'message': '<i>Нет места лучше дома. Вы принимаете решение вернуться домой и залечить свои раны в одному вам ведомом уюте.</i>'},
         23: {'button': 'Отказ от возвращения домой ✈️', 'msg': '<b>Отказ от возвращения домой</b>\nВаш путь ещё не закончен.', 'message': '<i>Подумав, вы понимаете, что настолько изменились в ходе этого путешествия, что дом - больше не дом для вас. Но это - уже другая история. Спасибо, Сказочник.</i>'},
         24: {'button': 'Свадьба 💒', 'msg': '<b>Свадьба, воцарение, финал</b>\nВы прошли долгий путь и заслужили быть любимым. Ведь это было той целью, что вела вас эти долгие дни?', 'message': '<i>Все, что хочется - вы получаете. Это - самый хороший финал из всех. И праздник, и пир, и свадьба, и сладкая ночь, и корона. Вы победили! И ваша история на этом заканчивается. Спасибо, Сказочник!</i>'},
         25: {'button': 'Неузнанное прибытие 🔕', 'msg': '<b>Неузнанное прибытие.</b>\nВы остаетесь неузнанно и спокойно жить свою жизнь.', 'message': '<i>Что может быть лучше покоя? Неузнанным вы возвращаетесь в родные пенаты, оставляя внутри ощущение завершенного дела и массу воспоминаний. Ваша история на этом заканчивается. Спасибо, Сказочник!</i>'},
         26: {'button': 'Узнавание 🤩', 'msg': '<b>Узнавание</b>\nВас узнают, но не приветствуют должным образом, что-то не так.', 'message': '<i>Что происходит? Да, вы вернулись, но что-то не так: вас узнают, но не оказывают должного почтения. Вам нужно разобраться, что пошло не так...</i>\n\n<b>Необоснованные притязания, которые предъявляют лжегерои.</b>\n<i>Кто-то решил присвоить ваши достижения себе, что-то снова обманывает и вводит в заблуждение. Похоже, снова нужно вновь отстаивать себя и свои интересы.</i>\n\n<b>Трудная задача</b>\n<i>Вот, что вам нужно сделать - пройти очередное испытание. В сказках обычно это то самое купание в молоке, от героя которое сварились.</i>\n\n<b>Задача решается.</b>\n<i>Вы - истинный герой!\nНо вы справляетесь и с этой непомерной задачей! Каким-то чужом или с помощью - решать вам. Вы - настоящий герой своей сказки!</i>\n\n<b>Свадьба, воцарение, хороший конец.</b>\n<i>Все, что хочется - вы получаете. Это - самый хороший финал из всех. И праздник, и пир, и свадьба, и сладкая ночь, и корона. Вы победили! И ваша история на этом заканчивается. Спасибо, Сказочник!</i>'},
         27: {'button': 'Погоня 🏎', 'msg': '<b>Погоня</b>\nНа вас открывают охоту.', 'message': '<i>Не тут-то было. На вас спускают всех собак, не думали же вы, что вас отпустят просто так? Бегите!</i>\n\n<b>Спасение от преследования</b>\n<i>Как и бывает в сказках, вы спасены. С помощью или без, хитростью или трусостью, но вы оказываетесь вдалеке от этих тревог. На этом ваша история заканчивается. Спасибо, Сказочник!</i>'},
         28: {'button': 'Поражение героя🪦', 'msg': '<b>Поражение героя</b>\nИногда сама победа в том, как много вы прошли и не сдались, а не то, смогли ли вы взойти на Олимп.', 'message': '<i>Вы терпите поражение. Но вы можете гордиться собой. Зайти так далеко может не каждый. Ваша история на этом кончается. Спасибо, Сказочник!</i>'},
         29: {'button': 'Возвращение домой 🏠', 'msg': '<b>Возвращение домой</b>\nВас ждут дома, пора идти.', 'message': '<i>Нет места лучше дома. Вы принимаете решение вернуться домой и залечить свои раны в одному вам ведомом уюте.</i><b>Неузнанное прибытие.</b>\n\n<i>Вы остаетесь неузнанно и спокойно жить свою жизнь.\nЧто может быть лучше покоя? Неузнанным вы возвращаетесь в родные пенаты, оставляя внутри ощущение завершенного дела и массу воспоминаний. Ваша история на этом заканчивается. Спасибо, Сказочник!</i>'},

         32: {'button': 'Создать новую историю 📚', 'msg': 'Отлично! Вперед, к новым приключениям!'},
         33: {'button': 'Вывод данных 📊', 'msg': 'Ваша сказка закончена. Вывести данные?'},
         101: 'Приветствую, сказочник!\n\nПеред тобой <b>бот-квест</b>, который поможет написать сказку. Тебе нужно только выбирать, куда повернёт сюжет сказки. В конце будет выведен весь путь героя, с помощью которого самостоятельно ты, Сказочник, напишешь своё произведение, подведёшь морали и придумаешь испытания на пути своего героя.\n\nВсе сказки строятся по нескольким шаблонам, команда Дома попыталась собрать большую часть в этой квест-игре. Твоя задача внимательно читать и выбирать кнопками ответ (кроме имени персонажа).\nИные способы ввода не будут работать.\n\nЕсли ты ошибся, то иди до конца со своей ошибкой.\nНет, серьёзно, у тебя будет возможность начать новую сказку, но тебе нужно закончить текущую, потому просто продолжай идти по сюжету или прокликай по кнопкам и после вывода данных выбери снова создание истории через команду /fable.\n\nУдачи! С любовью, команда Дома.'}
# 101: {'button': '', 'msg': '', 'message': ''},

#Статус -1 имеет доступ к 0, 1, 2 состоянию из таблицы story
HOOKUP = {-1: [0, 1, 2],
          0: [3, 4],
          1: [10, 11, 12, 13, 14], #отправка
          2: [10, 11, 12, 13, 14], #отправка
          3: [5, 6],
          4: [1, 2],
          5: [33, 7],
          6: [8, 9],
          7: [10, 11, 12, 13, 14], #отправка
          8: [10, 11, 12, 13, 14], #отправка
          9: [10, 11, 12, 13, 14], #отправка
          10: [15],
          11: [15],
          12: [18, 19],
          13: [16, 17],
          14: [18, 19],

          16: [18, 19],
          17: [18, 19],
          18: [20, 21],
          19: [29, 27, 21],
          20: [22, 23],
          21: [33],
          22: [24, 25, 26],
          23: [33],
          24: [33],
          25: [33],
          26: [33],
          27: [33],
          28: [33],
          29: [33],

          50: [32, 33],
          51: [18, 19],
          52: [16, 17],
          53: [32, 33],
          54: [18, 19],
          55: [16, 17]
          }


TEST = [['однажды в таверне...',  'https://uquiz.com/MeWQyx'],
        ['однажды на дороге...', 'https://uquiz.com/DBrx0e'],
        ['однажды дома...', 'https://uquiz.com/n9vHna'],
        ['Колесо фортуны', 'https://nameonwheel.com/ru/?input0=%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D1%8C&input1=%D0%9F%D1%80%D0%B8%D0%BD%D1%86&input2=%D0%93%D0%B5%D1%80%D0%BE%D0%B9&input3=%D0%9C%D0%B0%D0%B3&input4=%D0%9F%D0%BE%D0%BC%D0%BE%D1%89%D0%BD%D0%B8%D0%BA&input5=%D0%90%D0%BD%D1%82%D0%B0%D0%B3%D0%BE%D0%BD%D0%B8%D1%81%D1%82&input6=%D0%9B%D0%BE%D0%B6%D0%BD%D1%8B%D0%B9+%D0%B3%D0%B5%D1%80%D0%BE%D0%B9']]

TEST_RESULT = {'character_one': ['жадность', 'мстительность', 'милосердие', 'преданность', 'непоседа'],
               'character_two': ['настойчивость', 'бесстрашие', 'вера', 'оптимизм', 'дисциплина'],
               'character_three': ['любовь', 'жестокость', 'амбиции', 'честность', 'способность к убеждению'],
               'hero': ['принц', 'король', 'герой', 'маг', 'помощник', 'антагонист (враг)', 'ложный герой'],
               'setting': ['Русский фольклор', 'Киберпанк', 'Современность', 'Аниме', 'Фантастика (альтернативные вселенные, соулмейты, омегаверс и т.д.)', 'Мифология', 'Викторианская Англия (балы, рыцари, войны)', 'Племенные общины (лесные, островные; вожди, охотники, воины; ритуалы, обряды, традиции, Боги)', 'Постапокалипсис (зомби, погодны катаклизмы,  последствия ядерной войны и т.д.)', 'Мир абсурда (сны, badtrip, психологические искажения сознания)'],
               'answer_setting': ['Выбрать ✅', 'Посмотреть ещё 👀']

}

DESCRIPTION_HERO = {'принц': 'Воспитанный в достатке и покое, принц не нюхал пороху. Ваш герой - мальчик с золотой ложкой во рту, которому с самого детства все дозволено, а если что-то нет - без сомнения обаяния и манер хватит на то, чтобы выбить то, что хочется. Принц образован, начитан, но жизни не видел.',
               'король': 'Король - карающая и дающая длань, для кого-то - суровый правитель, для кого-то - изувер, для кого-то - отец и муж. Статная фигура по положению, что, определенно накладывает свой отпечаток на характер. Человек больше в возрасте, нежели чем молодой, главная его функция - направление и контроль.',
               'герой': 'Герой может быть любым как по качествам, так и по профессии. Главная его черта - неустроенность, которая и толкает его на путь героя. Какой-то внутренний конфликт или стечение обстоятельств, заставляющее двигаться прочь от зоны комфорта и побеждать!',
               'маг': 'Маг - это человек, обладающий суперсилами. Опытный, стойкий и образованный. В основном он и является дарителем чего-то сверхъестественного в каждой сказке, но теперь - это главный герой. Мудрость и знания дают ему определенный уровень холодности к превратностям судьбы и чужим жизням.',
               'помощник': 'Помощник - фигура интересная. От животного до человека, эта роль достается самым верным и преданным. Основная его цель - быть рядом с героем, сопровождать и защищать, пренебрегая своими амбициями, и всегда оставаться в тени. Но никто не отрицает, что помощник тоже может стать героем, потому что это - отдельная роль!',
               'антагонист (враг)': 'А вот и он - антагонист, человек со стойкими убеждениямид. Зло в чистом виде, без двойного дна, с руками по локоть в крови. В данном случае роль накладывает на себя такие установки, как: отрицательного в общем понимании персонажа, но настолько крепкого в собственной правоте, что скулы сводит, продуманность и рационализм.',
               'ложный герой': 'Ложный герой - роль с двойным дном. Неоднозначный персонаж, основной функцией которого является хитросплетенный обман главного героя. Но если поставить ложного героя на первое место, но можно сказать, что он расчетлив, хитер и опережает многих на два шага вперед. Часто двуличен, умен, обаятелен.',
                    }

DESCRIPTION_SETTING = {
                'Русский фольклор':
               '''<b>Королевство русского фольклора.</b>
Это королевство, где древние леса шепчут секреты через ветви деревьев, а реки несут в себе песни русалок. Богатыри бродят по земле, защищая слабых и сражаясь с чудовищами. Они собираются вместе на пирах, где звучат героические сказания, а кубки наполнены медом. На рынках торгуют амулетами и зельями, а кузнецы куют мечи, способные рассекать даже тени. В небе парят жар-птицы, озаряя ночь своим пламенем, а в глубинах лесов скрываются домовые и лешие, охраняя свои тайны.Это удивительная смесь ярких образов, героических подвигов, мистических существ и глубоких народных традиций. Это вселенная, где живут богатыри, обладающие сверхъестественной силой, и мудрые волшебники, способные управлять природными стихиями.
Русский фольклор также богат на песни, загадки, пословицы и поговорки, которые передаются из поколения в поколение и отражают мудрость и опыт народа. Эти истории и персонажи играют важную роль в культурном наследии и помогают сохранять национальную идентичность. Они вдохновляют на создание литературных произведений, кино и искусства, продолжая жить в современной культуре.''',
               'Киберпанк': '''<b>Королевство киберпанка.</b>
Это воображаемая вселенная, где технологии и компьютеризация достигли высочайшего уровня развития, но при этом общество страдает от коррупции, социального неравенства и экологических проблем. Это место, где высокие технологии сосуществуют с низким уровнем жизни большинства населения. Королевство, где технологии и человечество сливаются в одно целое. Это городские джунгли, где неоновые огни мерцают в вечной ночи, а небоскрёбы тянутся к небу, словно стальные гиганты. В этом мире информация — самый ценный ресурс. Персонажи киберпанка — это хакеры, киборги, искусственные интеллекты и уличные бойцы, которые пытаются выжить и найти свое место в этом хаотичном мире.
Хакеры проникают в защищённые сети, чтобы раскрыть корпоративные секреты и используют их для личной выгоды. Улицы заполнены киборгами и андроидами. В этом королевстве элита живёт в роскоши на вершинах небоскрёбов, в то время как бедняки и изгои скрываются в тёмных уголках на уровне улиц.
В киберпанке часто изображаются городские пейзажи, наполненные неоновыми вывесками, рекламными щитами, которые заслоняют небо, и улицами, переполненными людьми и разнообразными технологическими устройствами. Корпорации обладают огромной властью, зачастую превосходящей власть правительств, и контролируют жизнь граждан.''',
               'Современность': '''<b>Королевство современности</b>. 
Это эпоха, отмеченная стремительным технологическим прогрессом, глобализацией и социальными изменениями. Это время, когда информационные технологии и интернет изменили способы нашего общения, работы и развлечений. Здесь люди полагаются на свой ум, изобретательность и силу духа, чтобы прожить счастливую жизнь. Здесь высокие технологии и человеческие чувства идут на равне.
Пусть жизнь здесь богата и разнообразна, каждый житель стремится к тому, чтобы достичь чего-то, что не померкнет в рутине дел.
<b>Технологические инновации:</b>Современный мир характеризуется появлением передовых технологий, таких как искусственный интеллект, робототехника, биотехнологии и возобновляемые источники энергии. Эти технологии оказывают огромное влияние на экономику, здравоохранение и окружающую среду.
<b>Социальные изменения:</b>Современное общество постоянно эволюционирует, сталкиваясь с вызовами, такими как изменение климата, демографические сдвиги и борьба за социальную справедливость. Эти изменения ведут к новым формам политического активизма и общественного диалога.
<b>Культурное разнообразие:</b>Современный мир отличается культурным многообразием, где традиционные культуры сосуществуют и взаимодействуют с современными тенденциями. Это приводит к созданию новых культурных выражений и искусственных форм.
<b>Образование и наука:</b>Доступ к образованию становится всё более широким, а научные исследования продолжают расширять границы нашего понимания мира. Это ведёт к новым открытиям и инновациям, которые могут улучшить жизнь людей.
В целом, современный мир — это динамичное и сложное место, полное возможностей и вызовов, где каждый день приносит новые открытия и изменения. Это время, когда мы можем смотреть в будущее с надеждой и оптимизмом, стремясь к созданию лучшего мира для всех.''',
               'Аниме': '''<b>Королевство аниме</b>
Мир аниме — это яркая и разнообразная сфера японской анимации, которая охватывает множество жанров и стилей, отражая широкий спектр эмоций, тем и историй. Аниме не просто развлечение; это форма искусства, которая может варьироваться от лёгких и забавных сериалов до глубоких философских произведений, исследующих сложные человеческие вопросы.
<b>Жанры аниме</b>: Включают в себя широкий диапазон, такой как:
   1. <b>Сёнен(для молодых мужчин)</b>: Часто сосредоточены на приключениях, дружбе и соревнованиях.
   2. <b>Сёдзё(для молодых женщин)</b>: Обычно включают романтические или драматические сюжеты.
   3. <b>Сэйнэн</b> и <b>Дзёсэй</b>(для взрослых мужчин и женщин): Предлагают более зрелые темы и сложные сюжеты.
   4. <b>Меха</b>: Сосредоточены на роботах и технологиях.
   5. <b>Исэкай</b>: Персонажи попадают в параллельные миры или фэнтезийные вселенные.
   6. <b>Хоррор</b>: Исследуют тёмные и страшные темы.
<b>Визуальный стиль</b>: Аниме известно своим уникальным визуальным стилем, который включает в себя яркие цвета, преувеличенные эмоции и часто нереалистичные пропорции персонажей, особенно их большие выразительные глаза.
Это мир, где каждый может найти что-то для себя, независимо от возраста или интересов.''',
               'Фантастика (альтернативные вселенные, соулмейты, омегаверс и т.д.)': '''<b>Королевство фантастики</b>
Мир альтернативных вселенных — это концепция, которая захватывает воображение и стимулирует научные исследования. В этом мире каждая вселенная представляет собой уникальное измерение реальности, где могут действовать другие законы физики, история могла сложиться иначе, а возможности кажутся безграничными.
<b>Теория мультивселенной:</b> Согласно этой теории, существует бесконечное количество вселенных, каждая со своим набором параметров и начальных условий. Некоторые могут быть очень похожи на нашу, в то время как другие могут быть полностью неузнаваемыми.
<b>Параллельные вселенные:</b> Это альтернативные реальности, которые существуют одновременно с нашей и могут быть очень похожи или радикально отличаться. В некоторых теориях предполагается, что каждое решение создаёт новую параллельную вселенную.
<b>Альтернативная история:</b> В этих вселенных исторические события могли принять другой оборот, что привело бы к совершенно другим цивилизациям и технологиям. Например, если бы Римская империя никогда не пала, мир мог бы выглядеть совсем иначе.
<b>Фантастические вселенные:</b> В литературе и кино создаются вселенные, где магия является реальностью, а мифические существа сосуществуют с людьми. Примеры включают миры "Властелина колец" и "Гарри Поттера". Сюда же можно включить вселенные омегаверса и соулмейтов.
<b>Научно-фантастические вселенные:</b> Здесь технологии достигли уровней, о которых мы можем только мечтать, и человечество распространилось по всей галактике. Примеры включают вселенные "Звёздных войн" и "Звёздного пути".
Концепция альтернативных вселенных позволяет исследовать "что если" сценарии, предлагая бесконечные возможности для творчества, научных открытий и философских размышлений. Она напоминает нам, что реальность может быть гораздо более сложной и удивительной, чем мы можем себе представить.''',
               'Мифология': '''<b>Королевство мифологий</b>
Мир мифологий — это бесконечное поле для воображения, где каждая культура вносит свой уникальный вклад в ткань универсальных историй. Мифы отражают верования, страхи, надежды и мечты человечества, передаваясь из поколения в поколение и формируя основу культурного наследия народов.
<b>Греческая мифология:</b> Она полна героических подвигов, богов Олимпа и сложных сюжетов, где судьбы богов и людей тесно переплетены. Герои, такие как Геракл и Одиссей, и боги, такие как Зевс и Афина, стали символами человеческих качеств и архетипов.
<b>Скандинавская мифология:</b> Здесь в центре внимания стоят боги Асгарда, великие саги и конец света — Рагнарёк. Фигуры, такие как Один, Тор и Локи, играют ключевые роли в этих рассказах о мужестве, предательстве и судьбе.
<b>Египетская мифология:</b> Она полна богов с головами животных, фараонов, которые становятся богами после смерти, и сложных представлений о загробной жизни. Боги, такие как Ра, Осирис и Исида, управляют миром живых и мертвых.
<b>Индуистская мифология:</b> Это мир аватаров, богов и эпических поэм, таких как "Махабхарата" и "Рамаяна". Боги, такие как Вишну, Шива и Кали, представлены в многочисленных формах и проявлениях, каждая из которых имеет своё значение.
<b>Японская мифология:</b> Она включает в себя широкий спектр богов и духов (ками), а также рассказы о создании мира и островов Японии. Сюжеты часто связаны с природой и её явлениями.
<b>Ацтекская и майя мифология:</b> Эти мифологии изобилуют рассказами о создании мира, жертвоприношениях и богах, таких как Кецалькоатль и Тецкатлипока, которые влияют на судьбу человечества.
Мифологии мира также включают в себя многочисленные мифы африканских, австралийских аборигенов, американских индейцев и многих других культур, каждая со своими уникальными божествами, героями и мифами. Эти рассказы не только развлекают, но и несут в себе глубокие философские и моральные уроки, помогают людям понять мир и их место в нем.''',
               'Викторианская Англия (балы, рыцари, войны)': '''<b>Королевство Викторианской Англии.</b>
Викторианская Англия, охватывающая период правления королевы Виктории с 1837 по 1901 год, была эпохой значительных социальных, экономических и технологических изменений. Это было время промышленной революции, расширения Британской империи и значительных культурных разработок.
<b>Промышленность и технологии:</b> Промышленная революция достигла своего пика, и Англия стала мировым лидером в производстве и торговле. Появление железных дорог, паровых машин и телеграфа радикально изменило общество и экономику.
<b>Социальные различия:</b> Викторианская эпоха была также временем острых социальных контрастов. Роскошь и богатство аристократии и нового класса промышленников контрастировали с ужасающей бедностью рабочих районов и фабрик.
<b>Культура и литература:</b> Это был золотой век английской литературы, породивший таких писателей, как Чарльз Диккенс, Уильям Мейкпис Теккерей, Бронте и Оскар Уайльд.
<b>Мода и образ жизни:</b> Мода была формальной и отражала социальный статус. Мужчины носили фраки и цилиндры, а женщины — длинные платья с корсетами. Викторианский этикет был строгим, с акцентом на приличие и сдержанность.
<b>Архитектура:</b> Викторианская архитектура была разнообразной, от готического возрождения до классицизма. Здания часто были украшены изысканными деталями и орнаментами.''',
               'Племенные общины (лесные, островные; вожди, охотники, воины; ритуалы, обряды, традиции, Боги)': '''<b>Королевство племенных общин</b>
В мире племенных общин, будь то островные или лесные, жизнь тесно переплетена с природой и древними традициями. Эти общины часто управляются вождями, которые являются не только правителями, но и духовными наставниками.
<b>Островные племена</b> могут жить на отдаленных тропических островах, где белоснежные пляжи окружены кристально чистыми водами. Жизнь здесь следует ритмам приливов и отливов, а рыболовство и сбор плодов являются основными занятиями. Ритуалы часто связаны с морем, его дарами и его богами.
<b>Лесные племена</b> обитают в густых, непроходимых лесах, где деревья вздымаются к небу, как древние столпы. Они охотятся и собирают плоды, а их ритуалы часто связаны с духами леса, животными и растениями, которые считаются священными.
Воины в этих обществах обладают высоким статусом, они защищают племя от внешних угроз и участвуют в охоте. Они мастерски владеют оружием, изготовленным из доступных материалов, таких как дерево, кость и камень.
Ритуалы и церемонии играют ключевую роль в жизни племени, они могут включать танцы, пение и различные обряды инициации, которые отмечают важные события в жизни человека, такие как рождение, взросление, брак и смерть.
Вожди выбираются по различным критериям, в зависимости от традиций племени. Это может быть наследственная должность или выбор на основе мудрости, боевых заслуг или духовного видения.
Эти общины ценят гармонию с природой, силу сообщества и мудрость предков, которые передаются из поколения в поколение через рассказы и легенды.''',
               'Постапокалипсис (зомби, погодны катаклизмы,  последствия ядерной войны и т.д.)': '''<b>Королевство постапокалипсиса.</b>
В мире постапокалипсиса, где последствия ядерной войны, погодного катаклизма или смертоносного вируса оставили свой след, жизнь, какой мы её знаем, изменилась до неузнаваемости. Земля опустошена, и большинство городов превратились в руины. Небо покрыто пеплом, который скрывает солнце, создавая мрачный полумрак.
Здания и сооружения обветшали и разрушены, а улицы пусты, за исключением, быть может, странствующих зомби или иных форм новой жизни, которые бродят в поисках чего-то живого. Растительность увяла и погибла, оставив после себя лишь сухие пустыни и бесплодные земли. Вода загрязнена радиацией, и пить её без очистки опасно для здоровья.
Выжившие люди объединяются в небольшие группы, стремясь пережить каждый день, борясь за ограниченные ресурсы и защищаясь от зомби и других опасностей. Они создают убежища из обломков старого мира, используя всё, что могут найти, чтобы построить новое жильё и защититься от внешних угроз.
Это мир, где каждый день - это борьба за выживание, и каждый выбор может стать последним. Но даже в таких условиях люди находят способы сохранить человечность и надежду на лучшее будущее.''',
               'Мир абсурда (сны, badtrip, психологические искажения сознания)': '''<b>Королевство абсурда.</b> 
В мире снов и абсурда, где возможно всё, логика и законы физики подчиняются воле воображения. Это место, где небеса могут быть окрашены в зелёный цвет, а звёзды мерцают всеми оттенками радуги. Где люди могут плавать среди облаков, а рыбы летают среди звёзд. Горы из шоколада возвышаются над морями из лимонада, а деревья растут вверх ногами, их корни устремлены в небо.
В этом мире нет ничего невозможного:
   • Часы могут идти назад, давая второй шанс на прошедшие моменты.
   • Книги рассказывают истории, оживая перед читателем, персонажи выходят из страниц, чтобы поделиться своими приключениями.
   • Животные и предметы говорят человеческими голосами, делясь мудростью и шутками.
Это место, где каждый шаг может привести к новому измерению, и каждая мысль может стать реальностью. Мир снов и абсурда - это игровая площадка для души, где творчество не знает границ, а каждый день - это новое чудо.'''
}

FOTO_PATH = {'Русский фольклор': 'foto/russian.jpg',
             'Киберпанк': 'foto/cyberpunk.jpg',
             'Современность': 'foto/modernity.jpg',
             'Аниме': 'foto/anime.jpg',
             'Фантастика (альтернативные вселенные, соулмейты, омегаверс и т.д.)': 'foto/fantastic.jpg',
             'Мифология': 'foto/mythology.jpg',
             'Викторианская Англия (балы, рыцари, войны)': 'foto/Victorian.jpg',
             'Племенные общины (лесные, островные; вожди, охотники, воины; ритуалы, обряды, традиции, Боги)': 'foto/tribe.jpg',
             'Постапокалипсис (зомби, погодны катаклизмы,  последствия ядерной войны и т.д.)': 'foto/post.jpg',
             'Мир абсурда (сны, badtrip, психологические искажения сознания)': 'foto/absurd.jpg',
             'end': 'foto/end.jpg',
             'win': 'foto/win.jpg',
             'lose': 'foto/lose.jpg'
             }
