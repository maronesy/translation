# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 457 (printed ٤٥٦)."""

PAGE_NUMBER = 457
PRINTED_PAGE = "٤٥٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… وإنما اشترط أحدهما؛ لأن عمله لشبه المضارع،» at the foot of PDF p. 456.
    {"type": "matn",
     "ar": "فيلزم ألا يخالفه في الزمان نحو: «زيد ضارب غلامه عمرا الآن أو غدا»،",
     "en": "…so it must not differ from it in time, as in “Zayd is striking his slave ʿAmr now or tomorrow”."},
    {"type": "matn",
     "ar": "والمراد بالحال أو الاستقبال أعم من أن يكون تحقيقا أو حكاية، كقوله تعالى: ﴿وكلبهم باسط ذراعيه بالوصيد﴾[[١]]،",
     "en": "What is meant by the present or the future is more general than its being actual or narrated (ḥikāya), as in the words of the Exalted: “and their dog stretching out its forelegs at the threshold”;"},
    {"type": "matn",
     "ar": "فإن «باسط» ههنا وإن كان ماضيا، لكن المراد به حكاية الحال،",
     "en": "for “bāsiṭ” here, although it is past, is meant as the narration of a present state (ḥikāyat al-ḥāl);"},
    {"type": "matn",
     "ar": "ومعناها أن يقدر المتكلم باسم الفاعل العامل بمعنى الماضي، كأنه موجود في ذلك الزمان، أو يقدر ذلك الزمان كأنه موجود الآن.",
     "en": "its meaning is that the speaker supposes, with the governing active participle in the sense of the past, that he is as if present in that time, or supposes that time as if it were present now."},
    {"type": "matn",
     "ar": "(و) بشرط (الاعتماد) أي: اعتماد اسم الفاعل (على صاحبه) أي: على المتصف به،",
     "en": "(And) on condition of (reliance) (iʿtimād), that is, the active participle’s reliance (on its possessor), that is, on what is qualified by it,"},
    {"type": "matn",
     "ar": "وهو: «المبتدأ، أو الموصول، أو الموصوف، أو ذو الحال» ليتقوى فيه جهة الفعل من كونه مسندا إلى صاحبه",
     "en": "namely “the subject (mubtadaʾ), the relative noun (mawṣūl), the qualified noun (mawṣūf), or the possessor of the circumstantial state (dhū l-ḥāl)”, so that its verbal aspect is strengthened by its being predicated of its possessor,"},
    {"type": "matn",
     "ar": "نحو: «زيد ضارب أبوه»، و«جاء الضارب أبوه»، و«جاء رجل ضارب أبوه»، و«جاء زيد راكبا فرسه».",
     "en": "as in “Zayd, his father is striking”, “the one whose father is striking came”, “a man whose father is striking came”, and “Zayd came, his horse riding”."},
    {"type": "matn",
     "ar": "(و) اعتماده (على الهمزة) الاستفهامية ونحوها[[٢]] من ألفاظ الاستفهام (أو «ما» النافية) ونحوها من حروف النفي[[٣]] كـ«لا وإن»؛",
     "en": "(And) its reliance (on the hamza) of interrogation and the like among the interrogative words, (or the negative “mā”) and the like among the particles of negation, such as “lā” and “in”;"},
    {"type": "matn",
     "ar": "لأن الاستفهام والنفي بالفعل أولى، فازداد بهما شبهه بالفعل نحو: «أقائم زيد»، و«أقائم الزيدان»، و«ما قائم زيد»، و«ما قائم الزيدان».",
     "en": "because interrogation and negation belong more properly to the verb, so its resemblance to the verb is increased by them; as in “Is Zayd standing?”, “Are the two Zayds standing?”, “Zayd is not standing”, and “The two Zayds are not standing”."},
    {"type": "matn",
     "ar": "(فإن كان) اسم الفاعل المتعدي[[٤]] (للماضي) أي: للزمان الماضي بالاستقلال أو في ضمن الاستمرار، وأريد ذكر مفعوله[[٥]]",
     "en": "(If) the transitive active participle (is for the past), that is, for past time, independently or as included within continuance, and mention of its object is intended,"},
    {"type": "matn",
     "ar": "(وجبت الإضافة[[٦]]) أي: إضافة اسم الفاعل إلى مفعوله (معنى) أي: إضافة معنوية[[٧]]، لفوات شرط الإضافة اللفظية مثل: «زيد ضارب عمرو أمس»",
     "en": "(annexation is necessary), that is, the annexation of the active participle to its object, (in meaning), that is, a semantic annexation (iḍāfa maʿnawiyya), because the condition of verbal annexation (iḍāfa lafẓiyya) is lacking, as in “Zayd is the striker of ʿAmr yesterday”;"},
    {"type": "matn",
     "ar": "(خلافا للكسائي) فإنه ذهب إلى عدم وجوب إضافته؛ لأنه يعمل عنده سواء كان بمعنى الماضي، أو الحال، أو الاستقبال،",
     "en": "(contrary to al-Kisāʾī), for he held that its annexation is not necessary, because in his view it governs whether it has the sense of the past, the present or the future;"},
    {"type": "matn",
     "ar": "فيجوز أن يكون منصوبا على المفعولية، وعلى تقدير إضافته ليست إضافته معنوية؛ لأنها عنده من قبيل إضافة الصفة",
     "en": "so it [the object] may be in the accusative as an object, and on the supposition of its annexation, its annexation is not semantic, because in his view it is of the type of the annexation of the adjective…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الكهف: ١٨.",
     "en": "Qurʾān, Sūrat al-Kahf 18:18."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يشمل مثل: هل ضارب الزيدان ملفوظا أو مقدرا، نحو: قائم الزيدان أم قاعدان.",
     "en": "It includes such as “Are the two Zayds striking?” [with hal], whether uttered or implied, as in “Are the two Zayds standing or sitting?”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "صريحا أو مؤولا به نحو: إنما قائم الزيدان.",
     "en": "Explicit, or interpreted as such, as in “Only the two Zayds are standing” (innamā qāʾim al-Zaydān)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قيد به؛ لأن اسم الفاعل اللازم يرفع به مع كونه ماضيا.",
     "en": "He restricted it thus because the intransitive active participle gives the nominative by it [i.e., governs its agent] even while being past."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لأنه لو لم يذكر جاز أن لا يضاف نحو: هند ضاربة أمس.",
     "en": "Because if it is not mentioned, it may be left unannexed, as in “Hind was striking yesterday”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ولا ينصب إلا الظرف والجار والمجرور نحو: زيد ضارب أمس بالسوط؛ لأنه يكفيهما رائحة الفعل.",
     "en": "It puts nothing in the accusative except the adverb and the preposition with its object, as in “Zayd struck yesterday with the whip”, because a whiff of the verb suffices for them."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "بيان لحاصل المعنى.",
     "en": "An explanation of the resulting sense."},
    {"type": "pair",
     "ar": "وأما التركيب النحوي فهو إما تمييز أي: من حيث المعنى أو ظرف أي: في المعنى أو حال أي: ذات معنى أو مفعول مطلق أي: إضافة معنوية.",
     "en": "As for the grammatical construction, it is either a specification (tamyīz), that is, “in respect of meaning”; or an adverb (ẓarf), that is, “in meaning”; or a circumstantial state (ḥāl), that is, “having meaning”; or an absolute object (mafʿūl muṭlaq), that is, “a semantic annexation”."},
]
