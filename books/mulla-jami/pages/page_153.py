# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 153 (printed ١٥٢)."""

PAGE_NUMBER = 153
PRINTED_PAGE = "١٥٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "لكم﴾[[١]] (المجرد[[٢]] عن العوامل اللفظية) أي: الذي لم يوجد فيه عامل لفظي أصلا[[٣]].",
     "en": "…for you” (Qurʾān, Sūrat al-Baqara 2:184); (stripped of overt governors—al-mujarradu ʿani al-ʿawāmili al-lafẓiyyati), that is: that in which no overt governor (ʿāmil lafẓī) is found at all."},
    {"type": "matn",
     "ar": "واحترز به عن الاسم الذي فيه عامل لفظي كاسمي «إن» و«كان»،",
     "en": "By it he excluded the noun in which there is an overt governor, such as the nouns of “inna” and “kāna”;"},
    {"type": "matn",
     "ar": "وكأنه أراد بالعامل اللفظي: ما يكون مؤثرا في المعنى؛ لئلا يخرج عنه مثل: «بحسبك درهم».",
     "en": "and it is as if by “overt governor” he meant one that has an effect on the meaning, so that such as “A dirham suffices you” (bi-ḥasbika dirhamun) is not excluded from it."},
    {"type": "matn",
     "ar": "(مسندا إليه[[٤]]) واحترز به عن الخبر وثاني قسمي المبتدأ[[٥]] الخارج عن هذا القسم، فإنهما لا يكونان إلا مسندين",
     "en": "(As a subject of predication—musnadan ilayhi): by it he excluded the khabar and the second of the two kinds of mubtadaʾ, which falls outside this kind; for these two are only ever predicates;"},
    {"type": "matn",
     "ar": "(أو الصفة) سواء كانت مشتقة كـ«ضارب، ومضروب، وحسن» أو جارية مجراها كـ«قريشي»[[٦]]",
     "en": "(Or the adjective—awi al-ṣifatu), whether derived (mushtaqqa), like “ḍārib” (striking), “maḍrūb” (struck) and “ḥasan” (good), or treated like one, like “Qurayshī” (of Quraysh),"},
    {"type": "matn",
     "ar": "(الواقعة بعد حرف النفي) كـ«ما» و«لا»[[٧]] (وألف الاستفهام[[٨]]) ونحوه[[٩]] كـ«هل[[١٠]]، وما، ومن».",
     "en": "(occurring after a particle of negation—al-wāqiʿatu baʿda ḥarfi al-nafyi), like “mā” and “lā,” (and the alif of interrogation—wa-alifi al-istifhāmi) and the like, such as “hal,” “mā” and “man.”"},
    {"type": "matn",
     "ar": "وعن سيبويه جواز الابتداء بها من غير استفهام ونفي مع قبح، والأخفش يرى ذلك حسنا[[١١]]، وعليه قول الشاعر:",
     "en": "It is reported from Sībawayh that beginning with it without interrogation or negation is permissible, though unsightly (maʿa qubḥ); al-Akhfash considers that good; and upon this [view] is the poet’s saying:"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة البقرة، ١٨٤.",
     "en": "Qurʾān, Sūrat al-Baqara 2:184."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيل: إنما يصح لفظ التجريد مع أنه يقتضي سبق الوجود؛ لأن إمكان الوجود واحتماله قد ينزل منزلة الوجود،",
     "en": "It has been said: the word “stripping” (tajrīd) is valid, although it requires prior presence, only because the possibility and likelihood of presence may be treated as presence,"},
    {"type": "pair",
     "ar": "كقولك: ضيق فم الركية.",
     "en": "as in your saying: “Make the mouth of the well narrow.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: أن العبارة وإن كانت ظاهرة في سلب العموم، لكن المراد عموم السلب:",
     "en": "Meaning: although the wording is apparent in the negation of generality (salb al-ʿumūm), what is meant is the generality of the negation (ʿumūm al-salb):"},
    {"type": "pair",
     "ar": "إما باعتبار أن اللام أبطلت معنى الجمعية، فصار الجنس منفيا،",
     "en": "either on the consideration that the lām has cancelled the sense of plurality, so that the genus becomes negated;"},
    {"type": "pair",
     "ar": "أو باعتبار أن سلب العموم وإن كان أعم من عموم السلب، لكن المراد هو هذا بقرينة المقام.",
     "en": "or on the consideration that the negation of generality, although more general than the generality of negation, has the latter as what is meant, by the indication of the context."},
    {"type": "pair",
     "ar": "وأما القول بأن العبارة إن حملت على العدول أفاد عموم السلب، فغير ظاهر.",
     "en": "As for the claim that the wording, if construed as a metathetic [negation] (ʿudūl), yields the generality of negation, it is not evident."},
    {"type": "pair",
     "ar": "وإنما أكد النفي بقوله: «أصلا» ردا على من زعم أن المراد بالعوامل اللفظية نواسخ المبتدأ والخبر كـ«باب إن» وأخواته",
     "en": "He reinforced the negation with his word “at all” (aṣlan) only as a rejection of whoever claimed that what is meant by overt governors is the annulling agents (nawāsikh) of the mubtadaʾ and khabar, like “the category of inna” and its sisters,"},
    {"type": "pair",
     "ar": "لئلا ينتقض التعريف بقولك: «بحسبك درهم»،",
     "en": "so that the definition would not be broken by your saying: “A dirham suffices you” (bi-ḥasbika dirhamun);"},
    {"type": "pair",
     "ar": "وذلك لأن الذهن لا ينتقل من العوامل اللفظية إلى خصوص النواسخ.",
     "en": "and that is because the mind does not move from “overt governors” to the annulling agents specifically."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "حال من الضمير في «المجرد» الراجع إلى الاسم.",
     "en": "A circumstantial qualifier (ḥāl) of the pronoun in “al-mujarrad,” which refers back to the noun."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قد أشار به إلى أن المبتدأ مشترك معنوي لا أن لفظ المبتدأ مشترك لفظي، كما ذهب إليه الشيخ الرضي،",
     "en": "By it he indicated that “mubtadaʾ” is a semantically common term (mushtarak maʿnawī), not that the word mubtadaʾ is a homonym (mushtarak lafẓī), as al-Shaykh al-Raḍī held;"},
    {"type": "pair",
     "ar": "وإلا لزم استعمال اللفظ المشترك في معنيين.",
     "en": "otherwise it would follow that a homonymous word is used in two meanings [at once]."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فإنه في قوة: منسوب إلى قريش.",
     "en": "For it is equivalent to: “ascribed to Quraysh.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: وكذا \"إن\" النافية، نحو: «إن ضارب إلا زيد»، أي: ما ضارب إلا زيد،",
     "en": "That is: and likewise negating “in,” as in: “in ḍāribun illā Zaydun,” that is: “none is striking but Zayd”;"},
    {"type": "pair",
     "ar": "فـ«ضارب» مبتدأ وما بعده فاعله ساد مسد الخبر.",
     "en": "so “ḍārib” is a mubtadaʾ, and what follows it is its agent, filling the place of the khabar."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "الأولى حذف «الحرف» و«الألف» ليكون أخصر وأشمل،",
     "en": "It would have been better to omit “particle” and “alif,” so that it would be more concise and more comprehensive;"},
    {"type": "pair",
     "ar": "فيدخل \"إنما وغير وهل\" وغيرها من كلمات الاستفهام.",
     "en": "then “innamā,” “ghayr” and “hal” would be included, and other interrogative words."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "فذكر «الألف» للأصالة.",
     "en": "So the mention of “the alif” is because it is the basic [interrogative]."},
    {"type": "pair",
     "ar": "ولا يخفى أن مثل هذا الاعتبار لا يناسب التعريف.",
     "en": "It is not hidden that such a consideration does not suit a definition."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "وأين ومتى وكيف وكم وأيان التمثيل بـ\"هل\" وما ذكرناه ظاهر.",
     "en": "And “ayna,” “matā,” “kayfa,” “kam” and “ayyāna”; exemplification by “hal” and what we have mentioned is evident."},
    {"type": "pair",
     "ar": "وأما التمثيل بـ\"من\" فلا يصح بأن يقول: «من قائم أبوه»؛",
     "en": "As for exemplification by “man,” it is not valid by saying: “man qāʾimun abūhu” (Whose father is standing?);"},
    {"type": "pair",
     "ar": "لأن «قائم» صفة صالحة لأن تكون خبرا لـ«من»، وما يصلح أن يكون خبرا لا يصلح أن يكون مبتدأ.",
     "en": "because “qāʾim” is an adjective fit to be the khabar of “man,” and what is fit to be a khabar is not fit to be a mubtadaʾ [of this kind]."},
    {"type": "pair",
     "ar": "ولعل تمثيله بقولك: «من ضارب زيد» على أن \"من\" مفعول لـ«ضارب»، وقس عليه \"ما\".",
     "en": "Perhaps his exemplification is by your saying: “man ḍāribun Zaydun” (Whom is Zayd striking?), on the basis that “man” is the object of “ḍārib”; and judge “mā” by analogy with it."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "وكأن المصنف لم يعترف به،",
     "en": "It is as if the author did not acknowledge it;"},
    {"type": "pair",
     "ar": "فلهذا وللرد على من جعل أسماء الأفعال مبتدأة أتى بضمير الفصل الدال على حصر المبتدأ في الخبر،",
     "en": "so for this reason, and to reject whoever made verbal nouns (asmāʾ al-afʿāl) mubtadaʾs, he used the separating pronoun (ḍamīr al-faṣl), which indicates the restriction of the mubtadaʾ to the khabar;"},
    {"type": "pair",
     "ar": "فإنه قد يأتي لذلك كما صرح به شارح التلخيص.",
     "en": "for it sometimes comes for that, as the commentator on al-Talkhīṣ stated explicitly."},
]
