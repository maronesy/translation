# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 198 (printed ١٩٧)."""

PAGE_NUMBER = 198
PRINTED_PAGE = "١٩٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # continues from page 197 ("…واقصدوا خيرا")
    {"type": "matn",
     "ar": "لكم وهو التوحيد",
     "en": "…for you, namely the affirmation of [God’s] oneness (tawḥīd);"},
    {"type": "matn",
     "ar": "(وأهلا وسهلا[[١]]) أي: أتيت أهلا أي: مكانا مأهولا أي: معمورا لا خرابا، أو أهلا لا أجانب[[٢]] وطئت سهلا من البلاد لا حزنا.",
     "en": "(and “ahlan wa-sahlan”), that is: “you have come to a family (ahl),” that is, to an inhabited place, that is, one populated, not desolate; or “to family, not strangers”; “and you have trodden level (sahl) ground, not rough.”"},

    {"type": "section", "ar": "[المنادى]",
     "en": "The Vocative (al-Munādā)"},

    {"type": "matn",
     "ar": "(و) الموضع (الثاني) من تلك المواضع الأربعة (المنادى[[٣]]: وهو المطلوب إقباله[[٤]]) أي: توجهه إليك بوجهه أو بقلبه،",
     "en": "(And) the (second) place among those four is (the vocative—al-munādā: it is that whose turning towards [you] is sought), that is, its turning to you with its face or with its heart,"},
    {"type": "matn",
     "ar": "كما إذا ناديت مقبلا[[٥]] عليك بوجهه حقيقة، مثل: «يا زيد»",
     "en": "as when you call one who is turned towards you with his face in reality, as in: “O Zayd!” (yā Zaydu);"},
    {"type": "matn",
     "ar": "أو حكما مثل: ﴿يا سماء﴾[[٦]] و﴿يا جبال[[٧]]﴾[[٨]] و﴿يا أرض﴾[[٩]]،",
     "en": "or by status (ḥukman), as in: “O sky” (yā samāʾu), “O mountains” (yā jibālu) and “O earth” (yā arḍu);"},
    {"type": "matn",
     "ar": "فإنها نزلت أولا منزلة من له صلاحية النداء[[١٠]]، ثم أدخلت عليها حرف النداء، وقصد",
     "en": "for these were first treated as having the standing of one fit to be called; then the vocative particle was applied to them, and…was intended…"},

    {"type": "rule"},

    # ---------------- Footnote continued from page 197 (footnote ٩ there) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "الحذف لجواز ذكر الفعل معها. وإنما يجب إذا ترك الفعل في جميع الاستعمالات،",
     "en": "…of elision, since the verb may be mentioned with it. [Elision] is obligatory only when the verb is omitted in every usage,"},
    {"type": "pair",
     "ar": "نحو: «حسبك خيرا لك» أي: حسبك ما فعلت من هذا الأمر، و«ائت خيرا لك»",
     "en": "as in “ḥasbuka khayran laka,” that is: “Enough for you what you have done of this matter, and come to something better for you,”"},
    {"type": "pair",
     "ar": "و«وراءك أوسع لك» أي: تنح واقصد مكانا أوسع لك.",
     "en": "and “warāʾaka awsaʿa laka,” that is: “Move back, and aim at a place more spacious for you.”"},
    {"type": "pair",
     "ar": "ومن هذا القبيل عند الزمخشري: وانته أمرا قاصدا، أي: وسطا. وأما عند سيبويه، فلا.",
     "en": "Of this kind, according to al-Zamakhsharī, is “wa-ntahi amran qāṣidan” (and desist—a moderate course), that is: a middle one. According to Sībawayh, however, it is not."},
    {"type": "pair",
     "ar": "ولعله سمع ذكر فعله. إذا عرفت ذلك فالقول بوجوب الحذف في الآية الكريمة غير ظاهر.",
     "en": "Perhaps he heard its verb mentioned. Once you know this, the claim that elision is obligatory in the noble verse is not evident."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "عطف مثال على مثال.",
     "en": "The coordination of one example with another."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: كما جاز أن يكون صفة لـ«مكان» جاز أن يكون المراد أهل الشخص في مقابلة الأجانب جمع الأجنبي، فكأنك قلت: أتيت أهلك وأقاربك.",
     "en": "That is: just as it may be a qualifier of “place,” it may be that what is meant is a person’s family as opposed to strangers (ajānib, plural of ajnabī); so it is as if you said: “You have come to your family and your kin.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وهو كل مفعول به سمي منادى في الاصطلاح سواء كان لازم النداء في السعة، نحو: يا لكاع أو لا.",
     "en": "It is every direct object called “vocative” in technical usage, whether it is confined to the vocative in ordinary speech (fī al-saʿa), as in “yā lakāʿi” (O vile woman), or not."},
    {"type": "pair",
     "ar": "واعلم أن النداء بضم النون أو كسرها الصوت أو رفع الصوت. وذلك لأن ما كان على وزن فعال يجوز فيه الضم والكسر، نحو: نباح.",
     "en": "Know that nidāʾ, with ḍamma or kasra on the nūn, is the voice or the raising of the voice; this is because what is on the pattern fiʿāl admits both ḍamma and kasra, as in nubāḥ/nibāḥ (barking)."},
    {"type": "pair",
     "ar": "وقال السجاعي: النداء بالمد والقصر لغة: الدعاء، واصطلاحا: دعاء بحروف مخصوصة.",
     "en": "Al-Sujāʿī said: nidāʾ, with the long or the short vowel, means lexically “calling” (duʿāʾ), and technically a calling by means of particular particles."},
    {"type": "pair",
     "ar": "وقال أبو البقاء: الدعاء إحضار الغائب، وتنبيه الحاضر، وتوجيه المعرض، وتفريع المشغول، وتهييج الفارغ.",
     "en": "Abū al-Baqāʾ said: calling is summoning the absent, alerting the present, turning one who has turned away, freeing the occupied, and rousing the idle."},
    # REVIEW: print reads «وتفريع المشغول»; the sense suggests «وتفريغ المشغول»; transcribed as printed.

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: الاسم المطلوب إقباله، لكن تركه اكتفاء بما سبق من أنه لا بد من اعتبار الاسم.",
     "en": "That is: the noun whose turning is sought; but he left it out, contenting himself with what preceded, namely that “noun” must be taken into account."},
    {"type": "pair",
     "ar": "ويجوز أن يراد باللام الموصول، ويجعل كناية عن الاسم، وقدر المعنى في إقباله: أي: الاسم الذي طلب إقبال معناه.",
     "en": "It may be that the lām is meant as the relative and taken as an allusion to the noun, with “meaning” supposed in “iqbāluhu”: that is, the noun the turning of whose meaning is sought."},
    {"type": "pair",
     "ar": "ويجوز أن يكتفى على المسامحة المشهورة بإعطاء حال المعنى للفظ، وعدم تقدير المعنى أو بإعطاء حال اللفظ للمعنى، وعدم اعتبار الاسم في التعريف.",
     "en": "One may also rely on the well-known latitude of giving the state of the meaning to the word, without supposing “meaning”; or of giving the state of the word to the meaning, without taking “noun” into account in the definition."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "مفعول ناديت. وقيل: الإقبال التوجه مطلقا، أي بوجه أو بقلب أو غيرهما،",
     "en": "[Muqbilan is] the object of “nādayta.” It has been said: iqbāl is turning absolutely, that is, with the face, the heart or otherwise;"},
    {"type": "pair",
     "ar": "فيتناول لنداء الباري تعالى، وغير ذي الأرواح مما ليس بمنادى حقيقة، بل على سبيل التنزيل.",
     "en": "so it covers the calling of the Creator, the Exalted, and of things without souls, which are not vocatives in reality but by way of being so treated."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سورة هود: ٤٤.",
     "en": "Qurʾān, Sūrat Hūd 11:44."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "ولك أن تقول: إن نداء هؤلاء من باب التخييل لتشبيههما بمن له صلاح النداء.",
     "en": "You may say: calling these belongs to the category of imaginative figuration (takhyīl), because they are likened to one fit to be called."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "سورة سبأ: ١٠.",
     "en": "Qurʾān, Sūrat Sabaʾ 34:10."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "سورة هود: ٤٤.",
     "en": "Qurʾān, Sūrat Hūd 11:44."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "لسرعة امتثال الأمر.",
     "en": "Because of the swiftness with which the command is carried out."},
]
