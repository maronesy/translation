# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 399 (printed ٣٩٨)."""

PAGE_NUMBER = 399
PRINTED_PAGE = "٣٩٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «بل بعض معين، فكأنهم» at the foot of PDF p. 398.
    {"type": "matn",
     "ar": "اصطلحوا في باب المبنيات أن يريدوا بها ذلك البعض المعين، ولذلك لم يقل: «بعض الكنايات» كما قال: «بعض الظروف»،",
     "en": "…agreed, in the chapter on indeclinables, to mean by it that specific part; for that reason he did not say “some allusive nouns”, as he said “some adverbs (ẓurūf)”."},
    {"type": "matn",
     "ar": "ويتعذر تعريفه إلا بالتصريح به مفصلا، فلذلك أعرض عن تعريفها مطلقا، وتعرض لذلك البعض المعين، فقال: الكنايات:",
     "en": "It cannot be defined except by stating it explicitly in detail; therefore he refrained from defining them altogether and addressed that specific part, saying: allusive nouns are:"},
    {"type": "matn",
     "ar": "(«كم») وبناؤها لكونها موضوعة وضع الحروف[[١]]، أو لكون الاستفهامية متضمنة بمعنى الحرف، وحمل الخبرية عليها.",
     "en": "(“kam”): it is indeclinable because it is coined in the manner of particles, or because the interrogative [kam] contains the sense of a particle and the predicative (khabariyya) [kam] is assimilated to it."},
    {"type": "matn",
     "ar": "(و«كذا») وبناؤها؛ لأنها في الأصل «ذا» من أسماء الإشارة، دخل عليها كاف التشبيه، فصار المجموع بمنزلة كلمة واحدة بمعنى: «كم»[[٢]]، وبقي «ذا» على أصل بنائه،",
     "en": "(And “kadhā”): it is indeclinable because originally it is “dhā”, one of the demonstratives, to which the kāf of comparison was prefixed; the whole became like a single word meaning “kam”, and “dhā” remained in its original indeclinability."},
    {"type": "matn",
     "ar": "وكل واحد منهما يكون (للعدد) والكناية عنه، وجاء «كذا» كناية عن غير العدد أيضا، نحو: «خرجت يوم كذا» كناية عن يوم السبت أو غيره[[٣]].",
     "en": "Each of them is (for number) and for alluding to it; and “kadhā” also occurs as an allusion to something other than number, as in “I went out on such-and-such a day”, alluding to Saturday or another."},
    {"type": "matn",
     "ar": "(و«كيت» و«ذيت»[[٤]] للحديث) أي: للكناية عن الحديث والجملة،",
     "en": "(And “kayta” and “dhayta” are for speech), that is, for alluding to speech and to the sentence."},
    {"type": "matn",
     "ar": "وإنما بنيا؛ لأن كل واحد منهما[[٥]] كلمة واقعة موقع الجملة التي هي من حيث هي لا تستحق",
     "en": "They are indeclinable only because each of them is a word standing in the place of a sentence, which, as such, does not merit…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: وضعت ثنائية، ويسمى هذا الاسم اسما ناقصا.",
     "en": "That is, it was coined with two letters; such a noun is called a defective noun (ism nāqiṣ)."},
    {"type": "pair",
     "ar": "في القاموس: كم اسم ناقص مبني على السكون، أو مؤلفة من كاف التشبيه، وما قصرت وأسكنت وهي للاستفهام،",
     "en": "In al-Qāmūs: kam is a defective noun, indeclinable on sukūn; or it is composed of the kāf of comparison and mā, shortened and given sukūn. It is for interrogation,"},
    # REVIEW: «كم رجل كريم إياه هذا» is printed thus; the sense of «إياه» is unclear (a reading such as «أتاني» would be expected). Transcribed as printed.
    {"type": "pair",
     "ar": "وينصب ما بعده تمييزا وللخبر، ويخفض ما بعده كـ«رب»، وقد يرفع تقول: كم رجل كريم إياه هذا،",
     "en": "and what follows it is in the accusative as a specifier (tamyīz); and it is for predication (khabar), and what follows it is in the genitive, as with “rubba”; and it may be nominative: you say “kam rajulun karīmun iyyāhu hādhā” [as printed]."},
    {"type": "pair",
     "ar": "وقد يلوح من كلامه وجه آخر لبناء الاستفهامية وآخر لبناء الخبرية، فتأمل.",
     "en": "From his words there may appear one reason for the indeclinability of the interrogative and another for that of the predicative. So reflect."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: كناية عن العدد من غير اعتبار الاستفهام والتكثير.",
     "en": "That is, an allusion to number without regard to interrogation or to indicating abundance."},
    {"type": "pair",
     "ar": "ولذا لم يعتد بشيء منهما في المعنى، وليس لها الصدر تقول: قبضت كذا وكذا درهما، وغير واجب النصب، ولا يجوز جره بالإضافة ولا بـ«من»،",
     "en": "Hence neither of them is taken into account in its meaning, and it does not have the right to the head of the sentence: you say “I received kadhā wa-kadhā dirhaman”; [its specifier] is not necessarily accusative, and it may not be put in the genitive by annexation or by “min”;"},
    {"type": "pair",
     "ar": "ولا يتسعمل غالبا إلا مكررا معطوفا، فلا يقال: كذا درهما ولا كذا كذا درهما، بل يقال: كذا وكذا درهما.",
     "en": "and it is mostly used only repeated with coordination: one does not say “kadhā dirhaman” or “kadhā kadhā dirhaman”, but “kadhā wa-kadhā dirhaman”."},
    # REVIEW: «يتسعمل» is printed with transposed letters (for «يستعمل»); transcribed as printed.
    {"type": "pair",
     "ar": "وذكر ابن مالك أنه مسموع، لكنه قليل.",
     "en": "Ibn Mālik mentioned that it is attested, but rare."},
    {"type": "pair",
     "ar": "وفي القاموس: كذا اسم مبهم، وقد يجري مجرى «كم»، فينصب ما بعده على التمييز.",
     "en": "In al-Qāmūs: kadhā is a vague noun; it may be treated like “kam”, so that what follows it is put in the accusative as a specifier."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إما مجرور عطف على يوم السبت، أو مرفوع عطف على نحو، فإنه يجيء بمعنى كيت وكيت أيضا.",
     "en": "Either genitive, coordinated with “Saturday”, or nominative, coordinated with “naḥw”; for it also occurs in the sense of “kayta wa-kayta”."},
    {"type": "pair",
     "ar": "في القاموس: كيت وكيت ويكسر آخرهما أي: كذا وكذا، والتاء فيهما هاء في الأصل،",
     "en": "In al-Qāmūs: kayta wa-kayta, and their ends may take kasra, that is, “such and such”; the tāʾ in them was originally hāʾ."},
    # REVIEW: «كما في نبت» is printed thus; the parallel expected for a tāʾ replacing a dropped lām is «بنت». Transcribed as printed.
    {"type": "pair",
     "ar": "وتفصيله أنهما في الأصل: كيته وزيته على وزن المرة حذفت اللام وأبدل عنها تاء التأنيث كما في نبت.",
     "en": "In detail: originally they were kayyah and zayyah, on the pattern of the noun of single instance; the lām was dropped and the feminine tāʾ substituted for it, as in “nbt” [as printed; cf. bint]."},
    # REVIEW: «كيته وزيته» as printed («زيته» with zāy); transcribed as printed.
    {"type": "pair",
     "ar": "ومن العرب من يستعملها على الأصل والوقف عليها حينئذ بالهاء، ولا يكونان إلا مفتوحين، كذا في الرضي.",
     "en": "Some of the Arabs use it in its original form, the pause on it then being with hāʾ, and they are then always with fatḥa. So in al-Raḍī."},
    {"type": "pair",
     "ar": "وبين جواز بنائهما على الضم أيضا، ولزوم استعمالهما مكررتين بواو العطف.",
     "en": "He also explained that they may be indeclinable on ḍamma too, and that they must be used repeated with the coordinating wāw."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بفتح التاء وكسرها وقد تضم، أصلهما: كيه وذيه حذفت لام الكلمة، وعوض عنها التاء،",
     "en": "With fatḥa or kasra on the tāʾ, and it may take ḍamma. Their origin is kayyah and dhayyah: the final radical (lām al-kalima) was dropped and the tāʾ substituted for it;"},
    {"type": "pair",
     "ar": "ولذا تكتب طويلة، ويوقف عليها كما في أخت،",
     "en": "hence it is written long (as tāʾ, not tāʾ marbūṭa), and the pause is made on it as in “ukht”;"},
    {"type": "pair",
     "ar": "ولا يستعملان إلا مكررا بواو العطف نحو: قال فلان كيت وكيت، وكان ذيت وذيت.",
     "en": "and they are used only repeated with the coordinating wāw, as in “so-and-so said kayta wa-kayta” and “dhayta wa-dhayta happened”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لا يخفى أنه بهذا الوجه لا يصير من شيء من قسمي المبني لا من شابه مبني الأصل، ولا مما وقع غير مركب،",
     "en": "It is clear that by this reason it does not belong to either of the two kinds of indeclinable: neither to what resembles the originally indeclinable, nor to what occurs uncombined;"},
    {"type": "pair",
     "ar": "وله نظائر يرد عليك واحد بعد واحد، فلا تغفل.",
     "en": "and it has parallels that will come before you one after another; so do not be heedless."},
]
