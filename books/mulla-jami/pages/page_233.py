# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 233 (printed ٢٣٢)."""

PAGE_NUMBER = 233
PRINTED_PAGE = "٢٣٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "تفاوت (في مثل: «زيد قام وعمرا أكرمته») أي: عنده أو في داره ونحو ذلك[[١]]، وإلا لا يصح العطف على الصغرى لعدم الضمير",
     "en": "…difference, (in such as “Zayd stood, and ʿAmr—I honoured him”—Zaydun qāma wa-ʿAmran akramtuhu), that is, [I honoured him] at his place, or in his house, and the like; otherwise coordination with the minor [sentence] would not be valid, for lack of a [returning] pronoun."},
    {"type": "matn",
     "ar": "أي: يستوي الأمران فيما إذا عطف الجملة التي وقع فيها الاسم المذكور على جملة ذات وجهين، أي: جملة اسمية خبرها جملة فعلية،",
     "en": "That is: the two are equal when the sentence in which the noun mentioned occurs is coordinated to a sentence with two faces (jumla dhāt wajhayn), that is, a nominal sentence whose khabar is a verbal sentence;"},
    {"type": "matn",
     "ar": "فيصح رفعه بالابتداء ونصبه بتقدير الفعل، والوجهان مستويان، لحصول التناسب فيهما،",
     "en": "so its nominative by inchoation and its accusative by supposing the verb are both valid, and the two options are equal, since correspondence is achieved in both:"},
    {"type": "matn",
     "ar": "ففي الرفع تكون اسمية، فيعطف على الجملة الكبرى وهي اسمية، وفي النصب يكون فعلية، فيعطف على الجملة الصغرى وهي فعلية.",
     "en": "with the nominative it is nominal, and so is coordinated to the major sentence, which is nominal; with the accusative it is verbal, and so is coordinated to the minor sentence, which is verbal."},
    {"type": "matn",
     "ar": "فإن قلت: السلامة من الحذف مرجحة للرفع؟",
     "en": "If you say: is not freedom from elision a reason to prefer the nominative?"},
    {"type": "matn",
     "ar": "قلنا: هي معارضة بقرب المعطوف عليه[[٢]].",
     "en": "We say: it is countered by the nearness of the sentence coordinated to."},
    {"type": "matn",
     "ar": "فإن قلت: لا تفاوت في القرب والبعد بينهما؛ إذ الكبرى أيضا قريبة غير مفصولة عنها؟",
     "en": "If you say: there is no difference between them in nearness and distance, since the major [sentence] is also near and not separated from it?"},
    {"type": "matn",
     "ar": "قلنا: هذا باعتبار المنتهى[[٣]]، وأما باعتبار المبتدأ فالصغرى أقرب[[٤]].",
     "en": "We say: this is with respect to the end; with respect to the beginning, the minor is nearer."},
    {"type": "matn",
     "ar": "(ويجب النصب) أي: نصب الاسم المذكور (بعد حرف الشرط[[٥]]) والمراد به ههنا «إن ولو»،",
     "en": "(And the accusative is obligatory), that is, the accusative of the noun mentioned, (after a conditional particle); what is meant by it here is “in” and “law,”"},
    {"type": "matn",
     "ar": "فإن «أما» وإن كانت من حروف الشرط فحكمها ما سبق من اختيار الرفع مع غير الطلب واختيار النصب مع الطلب",
     "en": "for “ammā,” though it is among the conditional particles, has the status stated before: the nominative is preferred with something other than a request, and the accusative with a request."},
    {"type": "matn",
     "ar": "(و) كذا يجب نصبه بعد (حرف التحضيض) وهو: «هلا وألا[[٦]] ولولا ولوما»،",
     "en": "(And) likewise its accusative is obligatory after (a particle of urging—ḥarf al-taḥḍīḍ), namely “hallā,” “allā,” “lawlā” and “lawmā”;"},
    {"type": "matn",
     "ar": "وإنما وجب النصب بعدهما لوجوب دخولهما على الفعل[[٧]] لفظا أو تقديرا نحو: («إن زيدا ضربته ضربك») مثال لحرف الشرط (و«ألا",
     "en": "the accusative is obligatory after these two only because they must enter on the verb, in wording or by supposition, as in (“If Zayd—you strike him, he will strike you”—in Zaydan ḍarabtahu ḍarabaka), an example of the conditional particle, (and “allā…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإن قلت: فلا يصح كونه مما يستوي فيه الأمران لترجح الرفع باستغنائه عن تقدير نحو عنده",
     "en": "If you say: then it cannot be among the cases where the two are equal, since the nominative is preferable by dispensing with supposing something like “at his place,”"},
    {"type": "pair",
     "ar": "قلت: إذا كان المقصود إكرام عمرو عنده، فلا بد من تقدير عنده على تقدير الرفع أيضا.",
     "en": "I say: if what is intended is honouring ʿAmr at his place, then supposing “at his place” is necessary on the supposition of the nominative too."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ولك أن تقول: فالنصب مرجح باستغنائه عن تكلف جعل الجملة خبرا.",
     "en": "You may say: the accusative is then preferable through dispensing with the strain of making the sentence a khabar."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إذا جعل الجملة خبرا.",
     "en": "When the sentence is made the khabar."},
    {"type": "pair",
     "ar": "وأما إذا جعل الفعل وحده خبرا، واعتبر إسناده إلى المستتر الذي هو في حكم الملفوظ كما قيل في «زيد عرف» كانت الكبرى مفصولة باعتبار المنتهى الذي هو الضمير.",
     "en": "But when the verb alone is made the khabar, and its predication of the latent pronoun, which counts as uttered, is taken into account—as has been said of “Zaydun ʿarafa” (Zayd knew)—the major [sentence] is separated with respect to its end, which is the pronoun."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لم يعهد فيما بين أرباب العربية اعتبار مثل هذا القرب، ولا بد لاعتباره من شاهد.",
     "en": "Taking such nearness into account is not known among the masters of Arabic, and taking it into account requires evidence."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وما في حكمه من الأسماء الراسخة في الشرطية.",
     "en": "And the nouns that have its status, being firmly established as conditional."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "بالتشديد جوز الخليل فيها التخفيف.",
     "en": "With the doubled [lām]; al-Khalīl allowed the light form in it."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: لا شك أن التحضيض والعرض والاستفهام والنفي والشرط والتمني معان تليق بالفعل،",
     "en": "Shaykh al-Raḍī said: there is no doubt that urging, proposal, interrogation, negation, condition and wishing (tamannī) are meanings that befit the verb;"},
    {"type": "pair",
     "ar": "فكان القياس اختصاص حروفها بالأفعال إلا أن بعضها بقيت على ذلك الأصل كحروف التحضيض،",
     "en": "so analogy would have their particles be exclusive to verbs. But some of them remained on that original state, such as the particles of urging;"},
    {"type": "pair",
     "ar": "وبعضها اختصت بالاسمية كـ«ليت» و«لعل»، وبعضها استعملت في القبيلتين مع أولويتها بالأفعال كهمزة الاستفهام وما ولا للنفي،",
     "en": "some became exclusive to nominal [sentences], such as “layta” and “laʿalla”; some were used in both classes while being more appropriate to verbs, such as the hamza of interrogation and “mā” and “lā” of negation;"},
    # REVIEW: print reads «كـ«أل» للعرض»; the particle of proposal is presumably «ألا»; transcribed as printed.
    {"type": "pair",
     "ar": "وبعضها اختلف في اختصاصها كـ«أل» للعرض.",
     "en": "and about some there is disagreement over their exclusiveness, such as “al” [sic] of proposal."},
    # REVIEW: print reads «في أن امرؤ هلك»; the verse (Qurʾān 4:176) has «إن امرؤ هلك»; transcribed as printed.
    {"type": "pair",
     "ar": "وكذا «إن» الشرطية، فإن المرفوع في أن امرؤ هلك يجوز عند الأخفش أن يكون مبتدأ.",
     "en": "So too conditional “in”: the nominative in “in imruʾun halaka” (if a man perishes) (Qurʾān, Sūrat al-Nisāʾ 4:176) may, according to al-Akhfash, be a mubtadaʾ."},
]
