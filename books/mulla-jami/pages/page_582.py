# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 582 (printed ٥٨١)."""

PAGE_NUMBER = 582
PRINTED_PAGE = "٥٨١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «تفسير لـ«ما يوحى» الذي هو» at the foot of PDF p. 581.
    {"type": "matn",
     "ar": "المفعول الظاهر لـ«أوحينا».",
     "en": "…the explicit object of “awḥaynā”."},

    {"type": "section", "ar": "[حروف المصدر]",
     "en": "The Maṣdar-Forming Particles (ḥurūf al-maṣdar)"},

    {"type": "matn",
     "ar": "(حروف المصدر: «ما»، و«أن») المفتوحة المخففة (و«أن») المفتوحة المشددة.",
     "en": "(The maṣdar-forming particles: “mā”, “an”), with fatḥa and unstressed, (and “anna”), with fatḥa and stressed."},
    {"type": "matn",
     "ar": "(فالأولان) أي: «ما، وأن» المفتوحة المخففة (للفعلية) أي: للجملة الفعلية، أي: تدخلان على الجملة الفعلية، فتجعلانها في تأويل المصدر،",
     "en": "(The first two), that is, “mā” and the unstressed “an” with fatḥa, (are for the verbal), that is, for the verbal sentence; that is, they enter upon the verbal sentence and render it equivalent to a maṣdar,"},
    {"type": "matn",
     "ar": "نحو قوله تعالى: ﴿ضاقت عليهم الأرض بما رحبت﴾[[١]]، أي: برحبها -بضم الراء- وهو السعة،",
     "en": "as in His words, the Exalted: “the earth, for all its breadth (bi-mā raḥubat), became narrow for them”, that is, bi-ruḥbihā — with ḍamma on the rāʾ — which is spaciousness;"},
    {"type": "matn",
     "ar": "ونحو قولك: «أعجبني أن خرجت» أي: خروجك،",
     "en": "and as in your saying “aʿjabanī an kharajta” (that you went out pleased me), that is, your going out."},
    {"type": "matn",
     "ar": "واختصاص «ما» المصدرية بالفعلية إنما هو عند سيبويه، وجوز غيره بعدها الاسمية.",
     "en": "The restriction of maṣdar-forming “mā” to the verbal [sentence] holds only according to Sībawayh; others have allowed the nominal [sentence] after it."},
    {"type": "matn",
     "ar": "قال الشارح الرضي: وهو الحق وإن كان قليلا، كما وقع في نهج البلاغة، «بقوا في الدنيا ما الدنيا باقية».",
     "en": "The commentator al-Raḍī said: this is correct, even if it is rare, as occurs in Nahj al-Balāgha: “They remained in the world as long as the world remains (mā al-dunyā bāqiya).”"},
    {"type": "matn",
     "ar": "(وأن) المفتوحة المشددة (للاسمية) أي: للجملة الاسمية خاصة، إلا إذا كفت بـ«ما»، فيجوز بعدها الاسمية والفعلية.",
     "en": "(And anna), with fatḥa and stressed, (is for the nominal), that is, for the nominal sentence exclusively, unless it is restrained (kuffat) by “mā”, in which case both the nominal and the verbal may follow it."},
    {"type": "matn",
     "ar": "ومعنى كونها للاسمية أنها تعمل في جزأيها، وتجعلها في تأويل المفرد الذي هو مصدر خبرها،",
     "en": "The meaning of its being for the nominal [sentence] is that it governs its two parts and renders it equivalent to a single word, which is the maṣdar of its predicate,"},
    {"type": "matn",
     "ar": "نحو: «أعجبني أنك قائم» أي: قيامك، أو ما في معناه نحو: «أعجبني أن زيدا أخوك» أي: أخوة زيد،",
     "en": "as in “aʿjabanī annaka qāʾimun” (that you are standing pleased me), that is, your standing; or what is in its sense, as in “aʿjabanī anna Zaydan akhūka” (that Zayd is your brother pleased me), that is, Zayd’s brotherhood;"},
    {"type": "matn",
     "ar": "فإن تعذر قدرت الكون، نحو: «أعجبني أن هذا زيد» أي: كونه زيدا.",
     "en": "and if that is impossible, you supply “being” (al-kawn), as in “aʿjabanī anna hādhā Zaydun” (that this is Zayd pleased me), that is, its being Zayd."},

    {"type": "section", "ar": "[حروف التحضيض]",
     "en": "The Particles of Incitement (ḥurūf al-taḥḍīḍ)"},

    {"type": "matn",
     "ar": "(حروف التحضيض: «هلا»، و«ألا») مشددتين (و«لولا»، و«لوما» لها صدر الكلام)",
     "en": "(The particles of incitement: “hallā” and “allā”), both stressed, (“lawlā” and “lawmā”; they take the head of the sentence),"},
    {"type": "matn",
     "ar": "لدلالتها على أحد أنواع الكلام، فتصدر ليدل من أول الأمر على أن الكلام من ذلك النوع.",
     "en": "because they indicate one of the kinds of speech; so they are placed first, to indicate from the outset that the speech is of that kind."},
    {"type": "matn",
     "ar": "(ويلزمها الفعل) وفي بعض النسخ: «وتلزم الفعل» (لفظا) نحو: «هلا ضربت زيدا، وهلا تضرب زيدا»",
     "en": "(And the verb necessarily accompanies them) — in some copies: “and they necessarily accompany the verb” — (explicitly), as in “hallā ḍarabta Zaydan” (why did you not strike Zayd?) and “hallā taḍribu Zaydan” (why do you not strike Zayd?),"},
    {"type": "matn",
     "ar": "(أو تقديرا) نحو: «هلا زيدا ضربته[[٢]]، وهلا زيدا تضربه».",
     "en": "(or by implication), as in “hallā Zaydan ḍarabtahu” and “hallā Zaydan taḍribuhu”."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair", "ar": "سورة التوبة: ١١٨.", "en": "Qurʾān, Sūrat al-Tawba 9:118."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال الرضي: إذا وقع الظرف بعدها فهو منصوب بفعل بعده لا بفعل مقدر بعدها لتوسعهم في الظروف،",
     "en": "Al-Raḍī said: when an adverb of time or place (ẓarf) occurs after them, it is put in the accusative by a verb after it, not by a verb implied after them, because of their latitude with adverbs;"},
    {"type": "pair",
     "ar": "فنحو: هلا يوم الجمعة زرتني يوم الجمعة فيه منصوب بزرتني.",
     "en": "so in “hallā yawma al-jumuʿati zurtanī” (why did you not visit me on Friday?), “yawma al-jumuʿati” in it is in the accusative by “zurtanī”."},
]
