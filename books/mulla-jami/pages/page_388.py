# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 388 (printed ٣٨٧)."""

PAGE_NUMBER = 388
PRINTED_PAGE = "٣٨٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(إلا إذا) كانت موصولة (حذف صدر صلتها)» at the foot of PDF p. 387.
    {"type": "matn",
     "ar": "نحو قوله تعالى: ﴿ثم لننزعن من كل شيعة أيهم أشد على الرحمن عتيا﴾[[١]] فيمن قرأ بالضم[[٢]]، أي: أيهم هو أشد،",
     "en": "…as in His words, the Exalted: “Then We shall surely pluck out from every sect whichever of them was most obstinate against the All-Merciful”, according to those who read [ayyuhum] with ḍamma, that is, “ayyuhum huwa ashaddu” (whichever of them is most obstinate)."},
    {"type": "matn",
     "ar": "وإنما بنيت موصولة عند حذف صدر صلتها لتأكيد شبهه الحرف من جهة الاحتياج إلى أمر غير الصلة،",
     "en": "Relative [ayy] is made indeclinable when the first part of its relative clause is elided only because its resemblance to the particle is reinforced by its need of something other than the relative clause;"},
    {"type": "matn",
     "ar": "وبنيت على الضم تشبيها لها بالغايات؛ لأنه حذف منها بعض ما يوضحها كما حذف من الغايات ما يبينها، وهو المضاف إليه،",
     "en": "and it is made indeclinable with ḍamma to liken it to the “limit” words (al-ghāyāt), because part of what clarifies it has been elided from it, just as what explains the ghāyāt, namely the noun annexed to them, has been elided from them."},
    {"type": "matn",
     "ar": "ولم يستثن الموصوفة، لبنائه مثل: «يا أيها الرجل» كما استثنى التي حذف صدر صلتها؛",
     "en": "He did not make an exception of the qualified [ayy] on account of its indeclinability in such as “yā ayyuhā al-rajulu”, as he made an exception of the one whose relative clause has lost its first part,"},
    {"type": "matn",
     "ar": "لأنه ذكر في قسم المنادى أن كل ما يقع منادى مفردا معرفة فهو مبني، وبناء الموصوفة لهذا، فلا حاجة إلى الذكر ثانيا.",
     "en": "because he stated in the section on the vocative that everything that occurs as a single definite vocative is indeclinable, and the qualified [ayy] is indeclinable for this reason; so there is no need to mention it a second time."},
    {"type": "matn",
     "ar": "(وفي) قولهم: («ماذا صنعت؟»[[٣]] وجهان):",
     "en": "(In) their saying (“mādhā ṣanaʿta?” (what did you do?) there are two analyses):"},
    {"type": "matn",
     "ar": "(أحدهما:) إن معناه (ما الذي[[٤]]) على أن يكون «ذا» بمعنى الذي[[٥]]، فيكون التقدير: أي شيء الذي صنعت؟ أي: صنعته،",
     "en": "(the first of them) is that its meaning is (“mā alladhī”), on the view that “dhā” means alladhī, so that the implied form is: “What thing is that which you did?”, that is, “which you did it”;"},
    {"type": "matn",
     "ar": "فـ«ما» مبتدأ، وما بعده خبره، أو بالعكس",
     "en": "so “mā” is the subject and what follows is its predicate, or the reverse."},
    {"type": "matn",
     "ar": "(و) حينئذ (جوابه: رفع) أي: مرفوع على أنه خبر مبتدأ محذوف، كما إذا قلت: «الإكرام» أي: «الذي صنعته الإكرام»؛",
     "en": "(And) in that case (its answer is in the nominative), that is, it is nominative as the predicate of an elided subject, as when you say “al-ikrāmu” (honouring), that is, “alladhī ṣanaʿtuhu al-ikrāmu” (what I did is honouring),"},
    {"type": "matn",
     "ar": "ليكون الجواب مطابقا للسؤال في كون كل منهما جملة اسمية.",
     "en": "so that the answer corresponds to the question in each of them being a nominal sentence."},
    {"type": "matn",
     "ar": "(و) الوجه (الآخر) أن معناه (أي شيء)، وههنا عبارتان:",
     "en": "(And) (the other) analysis is that its meaning is (“ayyu shayʾin”) (what thing); here there are two formulations:"},
    {"type": "matn",
     "ar": "إحداهما: أن «ماذا» بكمالها بمعنى: «أي شيء».",
     "en": "the first, that “mādhā” as a whole means “ayyu shayʾin”;"},
    {"type": "matn",
     "ar": "والثانية: أن «ما» معناه: «أي شيء»، و«ذا» زائدة.",
     "en": "the second, that “mā” means “ayyu shayʾin” and “dhā” is redundant."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة مريم: ٦٩.",
     "en": "Qurʾān, Sūrat Maryam 19:69."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: عند بعض من قرأ بالضم، فإن منهم من جعله استفهاميا، وجعل الجملة صفة شيعة بتقدير مقول فيهم أيهم أشد.",
     "en": "That is, according to some of those who read it with ḍamma; for some of them made it interrogative and made the sentence a qualifier of “shīʿa”, with the implied sense “of whom it is said: which of them is most obstinate?”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: «ذا» لا تجيء موصولة ولا زائدة إلا بعد «ما ومن» الاستفهاميتين.",
     "en": "Shaykh al-Raḍī said: “dhā” does not occur as relative or as redundant except after interrogative “mā” and “man”."},
    {"type": "pair",
     "ar": "والأولى في ما ذا هو، ومن ذا خير منك الزيادة. ويجوز على بعد أن يكون بمعنى الذي أي: الذي هو خير منك على حذف المبتدأ.",
     "en": "The better view in “mā dhā huwa?” and “man dhā khayrun minka?” is redundancy. It may, though far-fetched, mean alladhī, that is, “who is it that is better than you?”, with the subject elided."},
    {"type": "pair",
     "ar": "وأما قولك: من ذا قائما، فـ«ذا» فيه اسم إشارة لا غير.",
     "en": "As for your saying “man dhā qāʾiman?” (who is this, standing?), “dhā” in it is a demonstrative and nothing else."},
    {"type": "pair",
     "ar": "ويحتمل في من ذا الذي أن تكون زائدة، وأن تكون اسم إشارة كما في قوله تعالى: ﴿أمن هذا الذي﴾ (الملك: ٢٠)، فإن هاء التنبيه تدخل على اسم الإشارة.",
     "en": "In “man dhā alladhī” it may be redundant, or it may be a demonstrative, as in His words, the Exalted: “Or who is this that…” (Qurʾān, Sūrat al-Mulk 67:20), for the hāʾ of drawing attention (hāʾ al-tanbīh) attaches to the demonstrative."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الجملة صفة لقوله: وجهان أو استئنافية.",
     "en": "The sentence is a qualifier of his word “two analyses”, or it begins anew (istiʾnāfiyya)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: ولقائل أن يمنع مجيء ذا موصولة، ويحكم في نحو: ماذا صنعت بزيادتها.",
     "en": "Shaykh al-Raḍī said: someone may deny that “dhā” occurs as a relative noun, and judge it redundant in such as “mādhā ṣanaʿta?”."},
    {"type": "pair",
     "ar": "إن قلت: رفع الجواب ورفع البدل عما يدل على أن الجملة اسمية؟",
     "en": "If you say: the nominative of the answer and the nominative of the substitute for it indicate that the sentence is nominal,"},
    {"type": "pair",
     "ar": "قلنا: جاز أن يكون «ما» مبتدأ و«ذا» مزيدة، والفعل خبر لما بتقدير العائد.",
     "en": "we say: “mā” may be the subject and “dhā” redundant, with the verb as the predicate of “mā”, a referring pronoun being supposed."},
    {"type": "pair",
     "ar": "وفيه أن حذف الضمير من خبر المبتدأ قليل دون صلة الموصول.",
     "en": "Against this: eliding the pronoun from the predicate of a subject is rare, unlike [eliding it from] the relative clause."},
]
