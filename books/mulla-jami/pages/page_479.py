# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 479 (printed ٤٧٨)."""

PAGE_NUMBER = 479
PRINTED_PAGE = "٤٧٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the analysis of «لا أرى» begun at the foot of PDF p. 478 (new sentence).
    {"type": "matn",
     "ar": "فعلى الأول: «واديا» مفعوله، و«كوادي السباع» حال منه قدم عليه.",
     "en": "On the first [reading], “wādiyan” is its object, and “ka-wādī al-sibāʿ” is a circumstantial qualifier (ḥāl) of it, placed before it."},
    {"type": "matn",
     "ar": "وعلى الثاني: «واديا» مفعوله الأول، و«كوادي السباع» مفعوله الثاني.",
     "en": "On the second, “wādiyan” is its first object, and “ka-wādī al-sibāʿ” its second object."},
    {"type": "matn",
     "ar": "وعلى التقديرين «حين يظلم» ظرف التشبيه المستفاد من الكاف،",
     "en": "On both readings, “ḥīna yuẓlimu” (when it grows dark) is an adverb of the comparison conveyed by the kāf;"},
    {"type": "matn",
     "ar": "والواو في «ولا أرى» إما اعتراضية[[١]]، أو حالية،",
     "en": "the wāw in “wa-lā arā” is either parenthetical (iʿtirāḍiyya) or circumstantial (ḥāliyya);"},
    {"type": "matn",
     "ar": "و«أقل» صفة «واديا»، والجار في «به»[[٢]] متعلق بـ«أقل»، والمجرور عائد إلى «واديا»،",
     "en": "“aqalla” is an adjective of “wādiyan”; the preposition in “bihi” is attached to “aqalla”, and its genitive object refers back to “wādiyan”;"},
    {"type": "matn",
     "ar": "و«ركب» فاعل «أقل»، وجملة «أتوه» صفة له،",
     "en": "“rakbun” is the agent (fāʿil) of “aqalla”, and the clause “atawhu” (who come to it) is an adjective of it;"},
    {"type": "matn",
     "ar": "و«تأية» تمييز عن نسبة «أقل» إلى «ركب»، أو منصوب على المصدرية أي: إتيانا تأية،",
     "en": "“taʾiyyatan” is a specification (tamyīz) of the attribution of “aqalla” to “rakb”, or it is in the accusative as a verbal noun, that is, “a coming of lingering”;"},
    {"type": "matn",
     "ar": "و«أخوف» عطف على «أقل»، وهو بمعنى المفعول[[٣]] أسند إلى ضمير واديا،",
     "en": "“akhwafa” is coordinated with “aqalla”; it has a passive sense and is predicated of the pronoun of “wādiyan”."},
    {"type": "matn",
     "ar": "والمعنى: واديا أقل به ركب منهم بوادي السباع وأخوف منه،",
     "en": "The meaning is: a valley in which riders linger less than they do in Wādī al-Sibāʿ, and more feared than it."},
    {"type": "matn",
     "ar": "و«ما» في «ما وقى الله» مصدرية، و«ساريا» أي: ركبا ساريا مفعول «وقى»،",
     "en": "“Mā” in “mā waqā Allāh” is the verbal-noun mā (maṣdariyya), and “sāriyan”, that is, a night-travelling rider, is the object of “waqā”;"},
    {"type": "matn",
     "ar": "والمستثنى مفرغ أي: واديا أقل وأخوف في كل وقت إلا في وقت وقاية الله تعالى ساريا،",
     "en": "and the exception is unfilled (mufarragh), that is: a valley lingered in less and more feared at every time, except at the time of Allah the Exalted’s protecting a night traveller."},
    {"type": "matn",
     "ar": "تقول[[٤]]: «مررت على وادي منسوب إلى السباع؛ لكثرتها فيها[[٥]]،",
     "en": "You say: “I passed by a valley attributed to the beasts of prey, because of their great number in it,"},
    {"type": "matn",
     "ar": "والحال أني لا أرى[[٦]] مثل وادي السباع حين أحاط به الظلام واديا يكون توقف الركب به أقل من توقفهم بوادي السباع،",
     "en": "while I see no valley like Wādī al-Sibāʿ when darkness has surrounded it, a valley in which the riders’ stopping is less than their stopping in Wādī al-Sibāʿ;"},
    {"type": "matn",
     "ar": "ويكون ذلك الوادي أخوف من وادي السباع في كل وقت، إلا في وقت وقاية الله سبحانه راكبا ساريا بالليل فيه عن الآفات[[٧]] والمخافات»،",
     "en": "and that valley is more feared than Wādī al-Sibāʿ at every time, except at the time when Allah, Glorified is He, protects a rider travelling in it by night from calamities and dangers.”"},
    # REVIEW: the two reformulations are printed identically («ولا أرى واديا أقل به ركب أتوه منه بوادي السباع»), although they are introduced as «العبارة الأولى» and «العبارة الثانية»; transcribed as printed.
    {"type": "matn",
     "ar": "ولو عبرت بالعبارة الأولى لقلت: «ولا أرى واديا أقل به ركب أتوه منه بوادي السباع»",
     "en": "Had you used the first expression, you would have said: “I see no valley in which riders who come to it linger less than they do in Wādī al-Sibāʿ”;"},
    {"type": "matn",
     "ar": "ولو عبرت بالعبارة الثانية لقلت: «ولا أرى واديا أقل به ركب أتوه منه بوادي السباع».",
     "en": "and had you used the second expression, you would have said: “I see no valley in which riders who come to it linger less than they do in Wādī al-Sibāʿ”."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لعل القول بالاعتراض بناء على أن بعد البيت شيئا متعلقا مررت،",
     "en": "Perhaps the view that it is parenthetical rests on there being something after the line that is attached to “marartu”;"},
    {"type": "pair",
     "ar": "فإن الاعتراض لا يكون إلا بين كلام أو كلامين متصلين معنى عند الجمهور لنكتة، وهي ههنا تفظيع شأن واد السباع.",
     "en": "for according to the majority a parenthesis occurs only within a statement, or between two statements connected in meaning, for a subtle purpose (nukta); here it is to make the state of Wādī al-Sibāʿ appear dreadful."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "والباء بمعنى «في».",
     "en": "The bāʾ has the sense of “fī” (in)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فإن الوادي مخوف فيه لا خائف إلا على الإسناد المجازي.",
     "en": "For the valley is that in which one is afraid, not that which is afraid, except by figurative attribution (al-isnād al-majāzī)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "نقل عنه حاصل معنى الشعر من أن توقف الركب في وادي السباع أقل من توقفهم في سائر الأودية،",
     "en": "He transmitted from him the gist of the poem’s meaning: that the riders’ stopping in Wādī al-Sibāʿ is less than their stopping in all other valleys,"},
    {"type": "pair",
     "ar": "وأن وادي السباع أخوف من كل واد إلا وقت وقاية الله تعالى الساري في وادي السباع.",
     "en": "and that Wādī al-Sibāʿ is more feared than every valley, except at the time when Allah the Exalted protects the night traveller in Wādī al-Sibāʿ."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "المراد بالسباع إما حقيقتها، أو شرار الناس وقطاع الطريق.",
     "en": "What is meant by “beasts of prey” is either their literal sense, or wicked people and highway robbers."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "جعل الواو حالية. وقيل: اعتراضية. وما ذكره أظهر.",
     "en": "He made the wāw circumstantial. It has also been said that it is parenthetical. What he mentioned is more evident."},
    {"type": "pair",
     "ar": "وإنما قال: ولا أرى. ومقتضى السياق أن يقول: وما رأيت ليفيد أنه ما أرى، ولا يرى قط؛",
     "en": "He said “wa-lā arā”, whereas the context required him to say “wa-mā raʾaytu”, only to convey that I do not see it, nor will it ever be seen;"},
    {"type": "pair",
     "ar": "لأنه لو أرى مثله لم يتأت منه الحكم بأنه لا يرى قط، فتأمل.",
     "en": "for if I saw its like, the judgement that it will never be seen could not be made. So reflect."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "متعلق بوقاية الله تعالى جل جلاله وعظم شأنه.",
     "en": "Attached to “the protection of Allah the Exalted”, majestic is His majesty and great His state."},
]
