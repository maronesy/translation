# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 203 (printed ٢٠٢)."""

PAGE_NUMBER = 203
PRINTED_PAGE = "٢٠٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues from p.202: «… ولم يعكس الأمر؛ لأن»
    {"type": "matn",
     "ar": "المنادى المستغاث واقع موقع كاف الضمير[[١]] التي يفتح لام الجر معها نحو: «لك»، بخلاف المستغاث له لعدم وقوعه موقع الضمير،",
     "en": "…the munādā called for help occurs in the position of the pronominal kāf, with which the genitive lām takes a fatḥa, as in “laka” (for you); unlike the mustaghāth lahu, since it does not occur in the position of the pronoun."},
    {"type": "matn",
     "ar": "فإن عطفت على المستغاث بغير «ياء» نحو: «يا لزيد، ولعمرو» وكسرت لام المعطوف؛",
     "en": "If you coordinate to the mustaghāth without “yāʾ,” as in “yā la-Zaydin wa-li-ʿAmrin,” you give the lām of the coordinated noun a kasra,"},
    {"type": "matn",
     "ar": "لأن الفرق بينه وبين المستغاث له حاصل بعطفه على المستغاث،",
     "en": "because the distinction between it and the mustaghāth lahu is secured by its being coordinated to the mustaghāth."},
    # REVIEW: the print vowels this second example with kasra on the lām of «ولعمرو», as in the first, though the rule stated requires fatḥa; transcribed (unvowelled) as printed.
    {"type": "matn",
     "ar": "وإن عطفت مع «يا» فلا بد من فتح لام المعطوف أيضا نحو: «يا لزيد، ولعمرو»،",
     "en": "If you coordinate with “yā,” then the lām of the coordinated noun must also take a fatḥa, as in “yā la-Zaydin wa-la-ʿAmrin” (O Zayd, and O ʿAmr, [help]!)."},
    {"type": "matn",
     "ar": "وإنما أعرب المنادى بعد دخول لام الاستغاثة؛ لأن علة بنائه[[٢]] كانت مشابهته للحروف، واللام الجارة من خواص الاسم،",
     "en": "The munādā became declinable after the lām of calling for help entered it only because the cause of its indeclinability was its resemblance to particles, while the genitive lām is among the properties of the noun;"},
    {"type": "matn",
     "ar": "فبدخولها ضعفت عليه مشابهته للحرف، فأعرب على ما هو الأصل فيه.",
     "en": "so by its entry its resemblance to the particle was weakened, and it was declined according to what is original in it."},
    {"type": "matn",
     "ar": "قيل: قد يخفض المنادى بلامي التعجب والتهديد[[٣]] أيضا،",
     "en": "It has been said: the munādā is also sometimes put in the genitive by the two lāms of wonder (taʿajjub) and threat (tahdīd)."},
    {"type": "matn",
     "ar": "فلام التعجب نحو: «يا للماء، ويا للدواهي»، ولام التهديد نحو: «يا لزيد لأقتلنك»،",
     "en": "The lām of wonder is as in “yā la-l-māʾi” (O, the water!) and “yā la-l-dawāhī” (O, the calamities!); the lām of threat is as in “yā la-Zaydin, la-aqtulannaka” (O Zayd, I shall surely kill you!)."},
    {"type": "matn",
     "ar": "فلم أهمل المصنف ذكرهما[[٤]]، وكيف يصدق[[٥]] قوله فيما بعد: «وينصب ما سواهما» كليا؟",
     "en": "So why did the author neglect to mention them, and how can his later words “and what is other than these two is put in the accusative” hold universally?"},
    {"type": "matn",
     "ar": "وأجيب[[٦]]: بأن كلا من هاتين اللامين لام الاستغاثة،",
     "en": "It was answered that each of these two lāms is the lām of calling for help:"},
    {"type": "matn",
     "ar": "كأن المهدد -اسم فاعل- يستغيث بالمهدد[[٧]] -اسم مفعول- ليحضر، فينتقم منه، ويستريح من ألم خصومته،",
     "en": "it is as though the one threatening (al-muhaddid, active participle) calls for help upon the one threatened (al-muhaddad, passive participle) so that he will come, and he will take revenge on him and find relief from the pain of his enmity;"},
    {"type": "matn",
     "ar": "وكأن المتعجب يستغيث بالمتعجب منه ليحضر، فيقضى منه التعجب، ويتخلص منه.",
     "en": "and as though the one who wonders calls for help upon the object of wonder so that it will come, and his wonder at it is fulfilled, and he is freed of it."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لو جعل هذا نكتة لفتح اللام من أول الأمر لكفى،",
     "en": "Had this been made the subtle reason for the fatḥa of the lām from the outset, it would have sufficed,"},
    {"type": "pair",
     "ar": "ولا يحتاج إلى دفع الالتباس بين المستغاث والمستغاث له الذي مادته أقل من القليل.",
     "en": "and there would be no need for removing the confusion between the mustaghāth and the mustaghāth lahu, whose occurrences are fewer than few."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إن قيل: دخول الجار على غير المنصرف لا يوجب صرفه، فكيف يوجب إعراب المبني؟",
     "en": "If it is said: the entry of a preposition on a diptote (ghayr al-munṣarif) does not make it fully declinable, so how does it make the indeclinable declinable?"},
    {"type": "pair",
     "ar": "أجيب عنه: بأن علة بنائه في غاية الضعف، وبأنه بدخول اللام صار بعيدا عما هو مدار الشبه وهو «يا»، خارجا عن الإفراد.",
     "en": "It was answered that the cause of its indeclinability is extremely weak, and that by the entry of the lām it became remote from what the resemblance turns on, namely “yā,” and left the condition of being single."},
    {"type": "pair",
     "ar": "وفيه أن البدل يبنى مع بعده، وأن الإفراد هنا في مقابلة الإضافة لا في مقابلة التركيب،",
     "en": "Against this: the substitute (badal) is made indeclinable despite its remoteness, and “being single” here is opposed to annexation, not to composition."},
    {"type": "pair",
     "ar": "ولا يبعد أن يجاب عنه: بأن حرف النداء واللام إذا اجتمعا كانت الغلبة للام لقربها، كما في تنازع الفعلين.",
     "en": "It is not far-fetched to answer that when the vocative particle and the lām come together, the upper hand belongs to the lām because of its proximity, as in the contention of two verbs (tanāzuʿ al-fiʿlayn)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: بلام تدخل على المنادى وقت التعجب أو وقت التهديد، فالإضافة لأدنى ملابسة.",
     "en": "That is: by a lām that enters the munādā at the time of wonder or the time of threat; so the annexation is for the slightest connection."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "اعتراض بأن المناسب ذكر هذا المنادى أيضا عند إرادة ذكر أنواع المنادى.",
     "en": "An objection: it would have been fitting to mention this munādā as well, when he intended to mention the kinds of munādā."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "اعتراض آخر بأنه عند عدم ذكر هذا المنادى في هذا المقام يلزم عدم صدق قوله فيما بعد، وينصب ما سواهما كليا مع أن الظاهر أنه قاعدة كلية.",
     "en": "Another objection: when this munādā is not mentioned in this place, it follows that his later words “and what is other than these two is put in the accusative” do not hold universally, although it appears to be a universal rule."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: print reads «مبنئ»; probably «منبئ» (indicative of); transcribed as printed.
    {"type": "pair",
     "ar": "أي: عن الاعتراضين، فما قيل: أو بأن قوله مثله: يا عبد الله من تتمة القاعدة مبنئ عن الغفلة.",
     "en": "That is: to the two objections. So what has been said—“or that his words ‘its like: yā ʿAbda llāh’ are part of the completion of the rule”—betrays heedlessness."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    # REVIEW: print reads «ليخصر»; probably «ليحضر» (so that he comes), as in the matn; transcribed as printed.
    {"type": "pair",
     "ar": "فيه أنه يأبى عن هذا التوجيه أن المتكلم بهذا النداء في حضور المهدد والمتعجب منه، وأنه لا معنى للاستغاثة بشيء ليخصر، فينتقم منه؛ لأنه لا يتصور الإغاثة منه،",
     "en": "Against this: this explanation is resisted by the fact that the one who utters this call is in the presence of the one threatened and of the object of wonder, and that there is no sense in calling for help upon something so that it comes and one takes revenge on it, since rescue from it is inconceivable."},
    {"type": "pair",
     "ar": "فالوجه أن يقال: يستغيث بالمهدد ليغير حاله، ويترك ما يوجب قتله أو ضربه، فيغيث المهدد، ويخلصه عن إثم القتل أو الضرب،",
     "en": "The right way is to say: he calls for help upon the one threatened so that he changes his state and abandons what calls for his being killed or beaten; thus he rescues the one threatening and frees him from the sin of killing or beating;"},
    {"type": "pair",
     "ar": "أو يستغيث به له بأن ينجي نفسه عن القتل بتغير أحواله وترك مساوي خصاله،",
     "en": "or he calls for help upon him for his own sake, that he save himself from being killed by changing his ways and abandoning the vices of his character;"},
    {"type": "pair",
     "ar": "ويستغيث بالمتعجب منه ليغيثه في التعجب المفرط الذي فوق طاقته، فيغير حاله، ويدفع عنه ما يوجب هذا التعجب.",
     "en": "and he calls for help upon the object of wonder so that it rescues him from excessive wonder beyond his capacity, by changing its state and removing from him what causes this wonder."},
]
