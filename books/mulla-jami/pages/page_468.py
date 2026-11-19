# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 468 (printed ٤٦٧)."""

PAGE_NUMBER = 468
PRINTED_PAGE = "٤٦٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… لا فرق بين الجهل والبلادة» at the foot of PDF p. 467 (mid-sentence).
    {"type": "matn",
     "ar": "والحمق[[١]]، ولكنهم حكموا بشذوذه في نحو: «أحمق من ابن هبنقة»[[٢]].",
     "en": "…and foolishness; yet they judged it anomalous in such as “aḥmaqu min Ibn Habanqa” (more foolish than Ibn Habanqa)."},
    {"type": "matn",
     "ar": "والجواب: بأن المراد بالحمق: ما يبدو من أثر البلادة في الظاهر،",
     "en": "The answer, that what is meant by foolishness is the trace of dullness that appears outwardly,"},
    {"type": "matn",
     "ar": "كما حكي عن ابن هبنقة من تعليق خرزات وعظام وخيوط على عنقه، وهو ذو لحية طويلة، فسئل عن ذلك، فقال: لأعرف بها نفسي ولا أضل،",
     "en": "as is related of Ibn Habanqa: he hung beads, bones and threads on his neck, though he had a long beard; asked about it, he said, “So that I may know myself by them and not get lost.”"},
    {"type": "matn",
     "ar": "وتقلد ذات ليلة أخوه بقلادته، فلما أصبح قال: «يا أخي أنت أنا، فمن أنا؟»",
     "en": "One night his brother put on his necklace, and in the morning he said, “Brother, you are I; then who am I?”"},
    {"type": "matn",
     "ar": "ففيه شائبة[[٣]] من حمق ابن هبنقة، فإنه يقتضي جواز اشتقاق «أحمق» من حمق لا يكون بهذا الظهور قياسا،",
     "en": "has a tinge of Ibn Habanqa’s foolishness; for it entails that deriving “aḥmaq” from a foolishness not so apparent is permitted by analogy,"},
    {"type": "matn",
     "ar": "وأن يكون اشتقاق «أجهل وأبلد» لمن يكون آثار جهله وبلادته ظاهرة على سبيل الشذوذ، ولا يقول بذلك عاقل.",
     "en": "and that deriving “ajhal” and “ablad” for one whose ignorance and dullness show outward traces is anomalous; and no sensible person holds that."},
    {"type": "matn",
     "ar": "والشارح الرضي عد «أحمق» من قبيل «أبلد» حيث قال:",
     "en": "The commentator al-Raḍī counted “aḥmaq” as of the same kind as “ablad”, where he said:"},
    {"type": "matn",
     "ar": "وينبغي أن يقال من الألوان والعيوب الظاهرة؛ فإن الباطنة يبنى منها أفعل التفضيل، نحو: «فلان أبلد من فلان وأحمق».",
     "en": "“One ought to say: from colours and outward defects; for from inward ones the elative afʿal is formed, as in ‘So-and-so is duller than so-and-so, and more foolish.’”"},
    {"type": "matn",
     "ar": "(وقياسه) أي: القياس الواقع[[٤]] في اسم التفضيل اشتقاقه (للفاعل) لا للمفعول،",
     "en": "(Its rule), that is, the analogical rule obtaining in the elative, is that it be derived (for the agent), not for the object;"},
    {"type": "matn",
     "ar": "فإنه لو اشتق[[٥]] لكل منهما قياسا مطردا لكثر الالتباس، فاقتصروا على الأشرف[[٦]].",
     "en": "for if it were derived for each of them by a regular rule, confusion would multiply; so they confined it to the nobler."},
    {"type": "matn",
     "ar": "(وقد جاء للمفعول) على خلاف القياس في مواضع قليلة (نحو: «أعذر») لمن هو أشد معذورية (و«ألوم») لمن هو أشد ملومية",
     "en": "(It has come for the object), against the rule, in a few places, (as in “aʿdhar”), for one who is more excused, (and “alwam”), for one who is more blamed,"},
    {"type": "matn",
     "ar": "(و) على هذا القياس («أشغل» و«أشهر» و«أعرف»).",
     "en": "(and), on this pattern, (“ashghal” (more occupied), “ashhar” (more famous) and “aʿraf” (better known))."},
    {"type": "matn",
     "ar": "(ويستعمل) أي: اسم التفضيل (على أحد ثلاثة أوجه[[٧]]) وهي: استعماله[[٨]]",
     "en": "(It is used), that is, the elative, (in one of three ways), namely: its use…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإن معناه: قلة العقل، فهو من العيوب الباطنة كالجهل.",
     "en": "For its meaning is lack of intelligence, so it is among the inward defects, like ignorance."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الصواب: من هبنقة بإسقاط الابن كما في المفصل وشرح التسهيل والحواشي الهندية والقاموس والصحاح وشمس العلوم.",
     "en": "The correct form is “min Habanqa”, dropping “Ibn”, as in al-Mufaṣṣal, Sharḥ al-Tashīl, the Indian glosses, al-Qāmūs, al-Ṣiḥāḥ and Shams al-ʿUlūm."},
    {"type": "pair",
     "ar": "والهبنق كعلمس الأحمق والقصير.",
     "en": "“Al-habanqaʿ”, on the pattern of ʿalamis, means the fool and the short man."},
    {"type": "pair",
     "ar": "وهبنقة لقب يزيد بن ثروان القيسي يضرب به المثل في الحمق من تعليق خرزات، ولذا يقال له: ذو الودعات،",
     "en": "Habanqa is the nickname of Yazīd ibn Tharwān al-Qaysī, proverbial for foolishness because of hanging beads; hence he is called Dhū l-Wadaʿāt (the man of the cowries),"},
    {"type": "pair",
     "ar": "فإن الودع متحركة خرزة بيضاء تخرج من البحر تعلق في عنق الصبيان لدفع العين.",
     "en": "for “wadaʿ”, with a vowelled [dāl], is a white bead brought out of the sea and hung on children’s necks to ward off the evil eye."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "خبر لقوله: والجواب المذكور أي: شائبة حمق صاحبه،",
     "en": "Predicate of his words “and the answer” mentioned, that is, a tinge of the foolishness of its author;"},
    {"type": "pair",
     "ar": "والفاء إما زائدة كما هو مذهب الأخفش، أو على تقدير أما.",
     "en": "the fāʾ is either redundant, as is the view of al-Akhfash, or on the supposition of an implied “ammā”."},
    {"type": "pair",
     "ar": "ذكر الشارح رحمه الله بيان لقبه المذكور في حواشي الهندية بعد هذا الجواب لا شنيع كما وهم.",
     "en": "The Commentator, may Allah have mercy on him, mentioned [this] as an explanation of his nickname mentioned in the Indian glosses after this answer, not as a rebuke, as has been wrongly supposed."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قدره بقرينة قوله: وقد جاء للمفعول.",
     "en": "He supplied it by the indication of his words “It has come for the object.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بخلاف الألفاظ المشتركة، فإنها مقصورة على السماع، فالالتباس فيها قليل.",
     "en": "Unlike homonymous words, which are restricted to attested usage, so confusion in them is slight."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "والأكثر فإن المفعول لا بد له من فاعل بخلاف الفاعل.",
     "en": "And the more frequent; for an object must have an agent, unlike the agent."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "إذ لم يكن معدولا، نحو: آخر أو اسما نحو: الدنيا، أو مخرجا عن المعنى التفضيلي نحو: آخر بمعنى غير.",
     "en": "When it is not deflected (maʿdūl), as in “ākhar”, or a noun, as in “al-dunyā”, or taken out of the elative sense, as in “ākhar” meaning “other”."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "يعني: أن الأوجه الثلاثة عبارة عن الاستعمالات الثلاثة.",
     "en": "He means that the three ways denote the three usages."},
    {"type": "pair",
     "ar": "فقوله: على أحد الوجوه الثلاثة حال من ضمير «يستعمل» أي: كائنا على أحد الاستعمالات الثلاثة.",
     "en": "So his words “in one of the three ways” are a circumstantial qualifier (ḥāl) of the pronoun in “is used”, that is, being in one of the three usages."},
]
