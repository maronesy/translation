# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 32 (printed ٣١)."""

PAGE_NUMBER = 32          # PDF page
PRINTED_PAGE = "٣١"       # page number printed in the book

BLOCKS = [
    # ---------------- The main commentary text (matn) ----------------
    {"type": "matn",
     "ar": "والكلم -بكسر اللام-: جنس[[١]] لا جمع، كـ«تمر وتمرة»[[٢]]، بدليل قوله تعالى:",
     "en": "Al-kalim — with a kasra on the lām — is a generic noun (jins), not a plural, like tamr (dates) and tamra (a single date); the proof being His words, the Exalted:"},
    {"type": "quran",
     "ar": "﴿إليه يصعد الكلم الطيب[[٣]]﴾[[٤]]",
     "en": "“Unto Him ascends the goodly word” (Qurʾān, Sūrat Fāṭir 35:10)."},
    {"type": "matn",
     "ar": "وقيل: جمع[[٥]]، حيث[[٦]] لا يقع إلا على الثلاث فصاعدا[[٧]].",
     "en": "It has [also] been said [to be] a plural, since it applies only to three or more."},
    {"type": "matn",
     "ar": "والكلم الطيب يؤول ببعض الكلم[[٨]].",
     "en": "And “the goodly word” (al-kalim al-ṭayyib) is figuratively construed as denoting some of the words (baʿḍ al-kalim)."},
    {"type": "matn",
     "ar": "واللام فيها[[٩]] للجنس[[١٠]]، والتاء للوحدة[[١١]]، ولا منافاة بينهما[[١٢]]، لجواز اتصاف",
     "en": "The lām in it denotes the genus (jins), while the tāʾ denotes the unit (waḥda); and there is no contradiction between the two, because it is permissible for [the genus to be qualified…]"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ههنا ثلاثة مذاهب:",
     "en": "Here there are three schools of thought:"},
    {"type": "pair",
     "ar": "أحدها: أنه اسم جنس، وهو المختار عند الجمهور، فيكون مفردا لفظا.",
     "en": "The first: that it [al-kalim] is a generic noun (ism jins), and this is the chosen [view] according to the majority; so it is singular in wording."},
    {"type": "pair",
     "ar": "ثانيها: أنه جمع، وإليه ذهب الزمخشري وصاحب اللباب.",
     "en": "The second: that it is a plural, and to this went al-Zamakhsharī and the author of al-Lubāb."},
    {"type": "pair",
     "ar": "ثالثها: أنه اسم جمع، نقلها الأزهري في التصريح عن بعضهم.",
     "en": "The third: that it is a collective noun (ism jamʿ); al-Azharī reported it in al-Taṣrīḥ from some [scholars]."},
    {"type": "pair",
     "ar": "وتحقيق ذلك يتوقف على بيان الفرق بين هذه الثلاثة.",
     "en": "Verifying this depends upon clarifying the difference between these three."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "والفرق بينه وبين التمر: بأنه لم يطلق إلا على الثلاث، بخلاف «التمر»، نشأ من الاستعمال حيث عرض للكلم هذا التخصيص، والتمر باق على وضعه.",
     "en": "The difference between it [al-kalim] and al-tamr is that it applies only to three [or more] — unlike “al-tamr” — [and this restriction] arose from usage, in that this specification happened to attach to al-kalim, whereas al-tamr remains upon its [original] coinage."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فإنه لو كان جمعا لوجب التأنيث، وبدليل أنه ليس من أوزان الجمع، لكونه مسندا إلى ضمير جمع غير العقلاء.",
     "en": "For had it been a plural, the feminine [agreement] would have been obligatory; and [a further] proof that it is not of the plural patterns is that it is predicated of a pronoun referring to a plural of non-rational beings."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة فاطر، ١٠.",
     "en": "Sūrat Fāṭir, [verse] 10."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وإليه ذهب الجوهري وصاحب اللباب وبعض من النحويين حيث قالوا: جمع الكلمة كلمات وكلم.",
     "en": "To this went al-Jawharī, the author of al-Lubāb, and some of the grammarians, who said: the plural of al-kalima is kalimāt and kalim."},
    {"type": "pair",
     "ar": "وقيل في التوفيق بين مذهب الجمهور وهذا القول: إن من قال: إنه ليس بجمع أراد أنه الجمع المستعمل في المعنى ليس بجمع بحسب اللفظ والوضع.",
     "en": "It has been said, in reconciling the school of the majority with this view: that whoever said “it is not a plural” meant that, although it is a plural used in [the sense of] meaning, it is not a plural with respect to wording and coinage;"},
    {"type": "pair",
     "ar": "ومن قال: إنه جمع أراد أنه مستعمل في معنى الجمع حيث لا يطلق إلا على ما فوق الاثنين.",
     "en": "and whoever said “it is a plural” meant that it is used in the sense of a plural, since it applies only to what is above two."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "كلمة «حيث» للتعليل.",
     "en": "The word “ḥaythu” [here] is for causation (taʿlīl)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "حال، وعامله محذوف، تقدير الكلام: لأنه لا يقع إلا على الثلاث، فيزاد ما يقع عليه هو صاعدا.",
     "en": "[It is] a circumstantial accusative (ḥāl), its governing word being elided; the implied sense of the speech being: “because it applies only to three, so that which it applies to is increased, [it being] ascending (ṣāʿidan).”"},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "فإن الصاعد إلى محل العرض ليس إلا بعض الكلم، وهو الطيب ككلمة التوحيد لا الخبيث، فجاز أن يعبر عنها ببعض الكلم،",
     "en": "For that which ascends to the locus of presentation is nothing but some of the words (baʿḍ al-kalim); and it is the goodly (al-ṭayyib), like the word of tawḥīd, not the wicked (al-khabīth); so it is permissible to express it by [the phrase] “some of the words.”"},
    {"type": "pair",
     "ar": "فتأويله كتأويل الرحمة بالإحسان في قوله تعالى: ﴿إن رحمت الله قريب من المحسنين﴾ (سورة الأعراف: ٥٦).",
     "en": "Its figurative interpretation is like the interpretation of “mercy” as “beneficence” in His words, the Exalted: “Indeed the mercy of Allah is near to the doers of good” (Qurʾān, Sūrat al-Aʿrāf 7:56)."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: في الكلمة.",
     "en": "That is: in [the word] al-kalima."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "هذا الوجه هو المختار؛ لأن المقام يقتضي تعريف المصطلح عليه، لا تعريف الفرد النوعي للمعنى اللغوي،",
     "en": "This aspect [the lām being for the genus] is the chosen one, because the context requires the definition of the technical term agreed upon, not the definition of the specific individual of the linguistic meaning;"},
    {"type": "pair",
     "ar": "أو لما يطلق عليه هذا اللفظ كما في صورة لام العهد الخارجي، ولا بيان الطرد حتى يكون اللام للاستغراق،",
     "en": "nor [the definition of] that to which this expression applies in the manner of the lām of external definite reference (lām al-ʿahd al-khārijī); nor [is it] the explication of coextension (ṭard) such that the lām would be for all-inclusiveness (istighrāq);"},
    {"type": "pair",
     "ar": "والتعريف ليس إلا للطبيعة من حيث هي، فاللام للجنس والطبيعة.",
     "en": "and the definition is only of the [pure] nature as such — so the lām is for the genus and the nature."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "ولقائل أن يمنع ذلك في المعنى العرفي، خصوصا عند من عدل في تعريف الكلمة عن اللفظة إلى اللفظ.",
     "en": "One could contest that in the customary [technical] meaning, especially according to one who, in defining al-kalima, shifted from al-lafẓa to al-lafẓ."},
    {"type": "pair",
     "ar": "وقال: الوحدة غير مرادة، ولئن سلم فيجوز القول بتجريدها عن معنى الوحدة،",
     "en": "And he said: unity (waḥda) is not intended; and even if it be granted, it is permissible to hold that it [the tāʾ] is stripped of the meaning of unity —"},
    {"type": "pair",
     "ar": "كما تجرد في مقام التعريف أسماء الأجناس عن الوحدة على تقدير وضعها للفرد المنتشر، وليس التاء نصا في الوحدة حتى يمتنع التجريد بدليل «كلمتين وتمرتين».",
     "en": "just as, in the setting of definition, the generic nouns are stripped of unity — on the assumption that they were coined for the dispersed individual; and the tāʾ is not explicit (naṣṣ) in [signifying] unity such that stripping [it] would be precluded, as evidenced by “kalimatayn” (two words) and “tamratayn” (two dates)."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "أي: بين التاء واللام، أن بين الجنس والوحدة.",
     "en": "That is: between the tāʾ and the lām — meaning that [there is no contradiction] between the genus and unity."},
]
