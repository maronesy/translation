# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 511 (printed ٥١٠)."""

PAGE_NUMBER = 511
PRINTED_PAGE = "٥١٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وهي:» at the foot of PDF p. 510 (mid-sentence).
    {"type": "matn",
     "ar": "«ظننت»، و«حسبت»، و«خلت») وهذه الثلاثة للظن[[١]].",
     "en": "…“ẓanantu”, “ḥasibtu” and “khiltu”); these three are for supposition (ẓann);"},
    {"type": "matn",
     "ar": "(و«زعمت») وهي تكون تارة للظن وتارة للعلم[[٢]].",
     "en": "(and “zaʿamtu”), which is sometimes for supposition and sometimes for knowledge;"},
    {"type": "matn",
     "ar": "(و«علمت»، و«رأيت»، و«وجدت») وهذه الثلاثة للعلم.",
     "en": "(and “ʿalimtu”, “raʾaytu” and “wajadtu”); these three are for knowledge."},
    {"type": "matn",
     "ar": "(تدخل) أي: هذه الأفعال (على الجملة الاسمية؛ لبيان ما هي) أي: تلك الجملة من حيث الإخبار بها ناشئة (عنه) من الظن والعلم",
     "en": "(They enter), that is, these verbs, (upon the nominal sentence, to make clear what it), that is, that sentence, insofar as it is asserted, (arises from), whether supposition or knowledge;"},
    {"type": "matn",
     "ar": "كما إذا قلت: «علمت زيدا قائما»، فقولك: «علمت» لبيان أن ما نشأت هذه الجملة عنه حين تكلمت بها وأخبرت بها عن قيام زيد، إنما هو العلم،",
     "en": "as when you say “ʿalimtu Zaydan qāʾiman” (I knew Zayd to be standing): your saying “ʿalimtu” makes clear that what this sentence arose from, when you uttered it and by it gave information about Zayd’s standing, is knowledge;"},
    {"type": "matn",
     "ar": "وإذا قلت: «ظننت زيدا قائما»، فقولك: «ظننت» لبيان أن منشأ الإخبار بهذه الجملة هو الظن، وكذلك بواقي الأفعال.",
     "en": "and when you say “ẓanantu Zaydan qāʾiman” (I supposed Zayd to be standing), your saying “ẓanantu” makes clear that the source of asserting this sentence is supposition; and likewise with the remaining verbs."},
    {"type": "matn",
     "ar": "(فتنصب) أي: هذه الأفعال (الجزأين) أي: جزئي الجملة الاسمية المسند والمسند إليه على أنهما مفعول لها[[٣]].",
     "en": "(So they put in the accusative), that is, these verbs, (the two parts), that is, the two parts of the nominal sentence, the predicate (musnad) and the subject (musnad ilayhi), as being an object of them."},
    {"type": "matn",
     "ar": "(ومن خصائصها) هي جمع «خصيصة»، وهي: ما يختص بالشيء ولا يوجد في غيره،",
     "en": "(And among their particular properties): [khaṣāʾiṣ] is the plural of “khaṣīṣa”, which is what is peculiar to a thing and not found in anything else;"},
    {"type": "matn",
     "ar": "أي: ومن خصائص أفعال القلوب (أنه إذا ذكر أحدهما ذكر الآخر) فلا يقتصر على أحد مفعوليها،",
     "en": "that is, among the particular properties of the verbs of the heart is (that when one of the two is mentioned, the other is mentioned), so one does not restrict oneself to one of their two objects."},
    {"type": "matn",
     "ar": "وسبب ذلك مع كونهما في الأصل مبتدأ وخبرا، وحذف المبتدأ والخبر غير قليل أن المفعولين معا بمنزلة اسم واحد؛ لأن مضمونهما معا هو المفعول به في الحقيقة[[٤]]،",
     "en": "The reason for this, though they are originally a subject and a predicate, and the elision of the subject and of the predicate is not rare, is that the two objects together stand in the position of a single noun, because their content together is in reality the direct object;"},
    {"type": "matn",
     "ar": "فلو حذف أحدهما كان كحذف بعض أجزاء الكلمة الواحدة، ومع هذا[[٥]] فقد ورد ذلك مع القرينة على قلة[[٦]].",
     "en": "so if one of them were elided, it would be like eliding some of the parts of a single word. Despite this, that has occurred, with a contextual indication (qarīna), though rarely."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "استعمالا شائعا وقليلا ما يستعمل على خلاف الأصل لفظ الظن في العلم، وأقل منه لفظ الحسبان والخيلة.",
     "en": "[That is,] in common usage; rarely is the word ẓann used, contrary to the basic sense, for knowledge, and still more rarely the words ḥisbān and khīla."},
    {"type": "pair",
     "ar": "ومن هذا النوع حجا يحجو للظن فقط، وهب غير متصرف بمعنى احسب وأرى المجهول وعد بمعنى حسب عند الكوفيين.",
     "en": "Of this kind are ḥajā, yaḥjū, for supposition only; hab, which is not inflected, in the sense of “iḥsib” (suppose); the passive urā; and ʿadda in the sense of ḥasiba, according to the Kūfans."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وهو كثير وإن كان بالنسبة إلى الظن قليلا.",
     "en": "And this is frequent, even if it is rare in comparison with [its use for] supposition."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: كل واحد منهما أو مجموعهما مفعول واحد لها من حيث المعنى، فإن علمت زيدا قائما معناه: علمت قيام زيد.",
     "en": "That is, each of them, or the two of them taken together, is a single object of them in terms of meaning; for “ʿalimtu Zaydan qāʾiman” means “I knew Zayd’s standing”."},
    {"type": "pair",
     "ar": "وفي بعض النسخ: مفعولان لها كما هو الظاهر.",
     "en": "In some copies: “two objects of them”, as is apparent."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: printed «عملت» in «فإن معنى عملت هذا زيدا», apparently a misprint for «علمت»; transcribed as printed, translated as «علمت».
    {"type": "pair",
     "ar": "والفعل المتعدي إليهما متعد إلى مفعول واحد في الحقيقة، وهو المصدر المأخوذ من المفعول الثاني المضاف إلى المفعول الأول، وإن كان جامدا،",
     "en": "The verb that is transitive to them is in reality transitive to a single object, namely the maṣdar taken from the second object and annexed to the first object, even if [the second] is non-derived (jāmid);"},
    {"type": "pair",
     "ar": "فإن معنى عملت هذا زيدا، علمت زيدية هذا.",
     "en": "for the meaning of “ʿalimtu hādhā Zaydan” (I knew this to be Zayd) is “I knew the Zayd-ness of this”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: مع وجود الدليل المانع من الحذف مطلقا وجد في استعمال حذف أحدهما مع القرينة، فلذا قلنا: إنه لا يجوز الاقتصار.",
     "en": "That is, despite the existence of the proof that prevents elision absolutely, the elision of one of them with a contextual indication is found in usage; for this reason we said that restriction [to one object] is not permitted."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: مع بقائه على المفعولية، وأما إذا حذف الفاعل وأقيم المفعول الأول مقامه، فهو واقع على كثرة كما مر في بحث المفعول به.",
     "en": "That is, with its remaining an object; but when the agent is elided and the first object put in its place, that occurs frequently, as has passed in the discussion of the direct object."},
]
